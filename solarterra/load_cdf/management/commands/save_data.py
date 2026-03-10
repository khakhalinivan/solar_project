from django.core.management.base import BaseCommand
import os
import datetime as dt
from django.conf import settings
from spacepy import pycdf
from load_cdf.models import *
from load_cdf.utils import *
from data_cdf.models import *
from solarterra.utils import ts_bigint_resolver as tbr
import timeit
import math
import numpy as np
from .evaluate_extras import command_logger, UploadRequired
from itertools import zip_longest
from django.db import connection


def save_single_file(cdf_file, fields, model_class, upload):

    t_total_start = timeit.default_timer()
    t_open_start = timeit.default_timer()
    cdf_obj = pycdf.CDF(cdf_file.full_path)
    t_open = timeit.default_timer() - t_open_start
    #print(cdf_file.full_path)
    arr_collection = []
    field_labels = []
    array_field_labels = set()
    fields_total = 0
    fields_with_data = 0
    fields_empty = 0
    empty_fields = []
    t_read = 0.0
    t_prepare = 0.0
    
    # numpy array work only
    for field in fields:
        fields_total += 1
        var = field.variable_instance
        #print(var.name, field.field_name)
        t_read_start = timeit.default_timer()
        if field.storage_mode == DynamicField.STORAGE_ARRAY:
            arr = cdf_obj[var.name][...]
        elif not field.multipart:
            arr = cdf_obj[var.name][...]
        else:
            # multipart can be either (records, parts) or a plain 1D array of parts
            raw = cdf_obj[var.name][...]
            part_index = field.multipart_index - 1

            if isinstance(raw, np.ndarray) and raw.ndim >= 2:
                #print(f"multipart: dims {var.dims}, dim_sizes {var.dim_sizes}, dim index {part_index}")
                arr = raw[:, part_index]
            elif isinstance(raw, np.ndarray) and raw.ndim == 1:
                if part_index >= raw.shape[0]:
                    make_log_entry(
                        f"multipart index {field.multipart_index} out of range for variable '{var.name}' with shape {raw.shape}",
                        "WARNING",
                        upload=upload,
                    )
                    continue
                arr = np.array([raw[part_index]])
            else:
                arr = np.array([raw])
        t_read += timeit.default_timer() - t_read_start
        
        t_prepare_start = timeit.default_timer()
        if len(arr) == 0:
            fields_empty += 1
            empty_fields.append((field.field_name, var.name))
            t_prepare += timeit.default_timer() - t_prepare_start
            continue
        fields_with_data += 1
            
        # there is no None numpy value for int types, and nan is a float
        # constructing python arrays will take up a lot more memory and time
        # so for now, i cast all numpy int array to object type to use None for invalid values
        
        if 'int' in str(arr.dtype):
            try:
                arr = arr.astype('object')
            except Exception as e:
                make_log_entry(f"Something went wrong during int to object array conversion: file '{cdf_file.full_path}' field '{field.field_name}': {e}", upload=upload)
                exit(1)

        # swap invalid datetime with None, everything else with np.nan
        if str(arr.dtype) == 'object':
            swap_value = None
        else:
            swap_value = np.nan
        
        # False will always propagate the other (significant) part of the OR operation
        condition = False
    
        #print("var: ", var.name, "fillval: ", var.fillval, "arr type", type(arr[0]), "fi", arr[0])
        # variable fillvals can differ from standard ones for the type: 017 command checks that
        # also fillval can change on the file level: #TODO add cdf file FILL_VAL and PAD_VALUE parsing here
        if var.fillval is not None:
            if isinstance(arr, np.ndarray):
                # For array-valued variables (e.g. spectrograms), use a scalar sample value for type conversion.
                if arr.size == 0:
                    make_log_entry(f"file '{cdf_file.full_path}' field '{field.field_name}' variable '{var.name}' contains an empty ndarray", "WARNING", upload=upload)
                    continue
                sample_value = arr.flat[0]
            else:
                sample_value = arr[0]

            fill_value = DataType.proper_type(var.fillval, sample_value)
            #print(f"FILL {fill_value}: {len(arr[arr==fill_value])} / {arr.shape}")
            #print("added fillval condition", var.fillval, type(arr[0]), fill_value, type(fill_value))
            if fill_value is None:
                make_log_entry("Could not parse fillval: file '{cdf_file.full_path}' variable '{var.name}' datatype '{data_type.cdf_file_label}', numpy type '{arr.dtype}'", "ERROR")
                exit(1)
            # choose values that are fillvals
            condition = condition | (arr == fill_value)
        
        # no parsing out values beyond valid interval: Maria`s request
        # that is happenning instead while plotting

        # check filter did not just stay False
        if isinstance(condition, np.ndarray):
            # filter all invalid values and swap them with nans
            arr[condition] = swap_value
        
        if 'float' in str(arr.dtype):
            nan_count = np.isnan(arr).sum()
            if nan_count > 0:
                make_log_entry(f"{nan_count} invalid values in '{field.field_name}' file '{cdf_file.full_path}'")
        
        # epoch parsing
        if field.data_type_instance.is_epoch():
            arr_collection.append(map(tbr, arr))
        else:
            arr_collection.append(arr)

        # add attribute name for arrays with only non-zero entry counts
        field_labels.append(field.field_name)
        if field.storage_mode == DynamicField.STORAGE_ARRAY:
            array_field_labels.add(field.field_name)
        t_prepare += timeit.default_timer() - t_prepare_start
    
    

    # zip by longest array instead of shrotest as in classic zip
    # only needed here as temporary solution for different depend fields (epochs) with different lengths
    t_rows_start = timeit.default_timer()
    zipped_collection = zip_longest(*arr_collection)
    insert_rows = []
   
    
    for collection_row in zipped_collection:
        row_values = dict(zip(field_labels, collection_row))
        for field_label in array_field_labels:
            value = row_values.get(field_label)
            if value is None:
                continue
            if isinstance(value, np.ndarray):
                row_values[field_label] = value.tolist()
            elif isinstance(value, tuple):
                row_values[field_label] = list(value)
        row_values["cdf_file_id"] = cdf_file.id
        insert_rows.append(row_values)
    t_rows = timeit.default_timer() - t_rows_start
    
    t_insert_start = timeit.default_timer()
    use_raw_insert = getattr(settings, "SAVE_DATA_USE_RAW_INSERT", True)
    if use_raw_insert and len(insert_rows) > 0:
        table_name = model_class._meta.db_table
        columns = list(field_labels) + ["cdf_file_id"]
        required_cols = set(columns)
        for row_index, row in enumerate(insert_rows):
            missing_cols = [col for col in columns if col not in row]
            extra_cols = set(row.keys()) - required_cols
            if missing_cols or extra_cols:
                make_log_entry(
                    (
                        f"Row shape mismatch before raw insert for file '{cdf_file.full_path}', row {row_index}: "
                        f"missing={missing_cols}, extra={sorted(extra_cols)}"
                    ),
                    "ERROR",
                    upload=upload,
                )
                exit(1)

        placeholders = ", ".join(["%s"] * len(columns))
        col_sql = ", ".join([f"\"{col}\"" for col in columns])
        sql = f"INSERT INTO \"{table_name}\" ({col_sql}) VALUES ({placeholders})"
        values = [tuple(row.get(col) for col in columns) for row in insert_rows]
        with connection.cursor() as cursor:
            cursor.executemany(sql, values)
    elif len(insert_rows) > 0:
        instances = [model_class(**row) for row in insert_rows]
        model_class.objects.bulk_create(instances, batch_size=2000)
        del instances

    cdf_file.update(loaded=True, saved_rows=len(insert_rows)) 
    t_insert = timeit.default_timer() - t_insert_start
    print(len(insert_rows)) 
    del arr_collection
    del zipped_collection
    del insert_rows
    
    cdf_obj.close()

    if fields_empty > 0:
        preview = ", ".join([f"{f}/{v}" for f, v in empty_fields[:8]])
        if fields_empty > 8:
            preview += ", ..."
        make_log_entry(
            f"file '{cdf_file.full_path}' has {fields_empty} empty fields: {preview}",
            "WARNING",
            upload=upload,
        )

    t_total = timeit.default_timer() - t_total_start
    make_log_entry(
        (
            f"profile save_single_file '{cdf_file.full_path}': "
            f"fields total={fields_total}, with_data={fields_with_data}, empty={fields_empty}, "
            f"rows={cdf_file.saved_rows}; "
            f"timings sec open={t_open:.4f}, read={t_read:.4f}, prepare={t_prepare:.4f}, "
            f"rows={t_rows:.4f}, insert={t_insert:.4f}, total={t_total:.4f}"
        ),
        "INFO",
        upload=upload,
    )

class Command(UploadRequired, BaseCommand):

    help = "Command to load all data from the saved cdf files."

    requires_migrations_checks = True


    def add_arguments(self, parser):
        parser.add_argument("upload_tag", nargs=1, type=str)
        parser.add_argument("dataset_tag", nargs=1, type=str)
    
    @command_logger
    def handle(self, *args, **options):
        
        upload_tag = options["upload_tag"][0]
        dataset_tag = options["dataset_tag"][0]
        try:
            upload = Upload.objects.get(u_tag=upload_tag, dataset__tag=dataset_tag)
        except:
            make_log_entry(f"Upload instance with upload_tag {upload_tag} and dataset_tag {dataset_tag} is not found.", "EXIT")
            exit(0)

        try:
            dynamic_model_instance = dmi = upload.dataset.dynamic
        except Exception as e:
            make_log_entry(f"Retrieving dynamic model instance: {e}", "ERROR", upload=upload)
            upload.terminate()

        try:
            model_class = dmi.resolve_class()
        except Exception as e:
            make_log_entry(f"Retrieving data model class: {e}", "ERROR", upload=upload)
            upload.terminate()
        
        if model_class is None:
            make_log_entry(f"Model class '{dmi.model_name}' is not found.", "ERROR", upload=upload)
            exit(1)
        else:
            make_log_entry(f"Resolved data model class '{dmi.model_name}'", "SUCCESS", upload=upload)

        
        cdf_files = upload.cdf_files.all()
        if cdf_files.count() == 0:
            make_log_entry("No files found to upload.", upload=upload)
            exit(1)
        else:
            make_log_entry(f"{cdf_files.count()} files are to be uploaded to the db.", upload=upload)

        fields = dmi.fields.order_by('variable_instance__depend_0', 'multipart', 'multipart_index')

        file_count = cdf_files.count()
        percent = 0
        deltas = []


        for index, cdf_file in enumerate(cdf_files):
            if cdf_file.loaded:
                make_log_entry(f"File '{cdf_file.full_path}' is supposed to be loaded with {cdf_file.saved_rows}, skipping", upload=upload)
                continue
            t1 = timeit.default_timer() 
            save_single_file(cdf_file, fields, model_class, upload)
            t2 = timeit.default_timer() 
            deltas.append(t2 - t1)

            current_percent = math.floor(index / file_count * 100)
            
            if current_percent > percent:
                make_log_entry(f"{current_percent}% done, {index + 1} files uploaded, total time {round(sum(deltas), 5)}, avg time per file {round(sum(deltas) / len(deltas), 5)}", upload=upload)
                print(f"{current_percent}% done, {index + 1} files uploaded, total time {round(sum(deltas), 5)}, avg time per file {round(sum(deltas) / len(deltas), 5)}")
                percent = current_percent





    
