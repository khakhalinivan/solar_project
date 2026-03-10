from load_cdf.models import *
from solarterra.utils import ts_bigint_resolver as ti
from solarterra.utils import bigint_ts_resolver as it
from solarterra.utils import str_to_dt

import math
import datetime as dt
import numpy as np
from pages.figures import scatter, n_trace, spectrogram


class DBQuery():


    def __init__(self, dataset, filter_field, t_start, t_stop, fields):

        # instance
        self.dataset = dataset
        # class
        self.data_class = dataset.dynamic.resolve_class()

        # time strings
        self.start_limit = ti(t_start)
        self.stop_limit = ti(t_stop)

        # field (instance) on which the filtering happens
        self.filter_field = filter_field
        self.fields = fields
        # 0th position of the filter_field is important
        self.all_fields = [filter_field] + fields

        # not evaluated queryset
        self.queryset = None
        # transposed and sorted arrays of values
        self.arrays = None

        # bin mapping over over the array of epochs
        self.bin_map = None


    def query(self):
        kwargs = {
            '{0}__gte'.format(self.filter_field): self.start_limit,
            '{0}__lte'.format(self.filter_field): self.stop_limit,
        }
        self.queryset = self.data_class.objects.filter(**kwargs)
    
    # alternative way ?
    """
    def evaluate(self):sorted_pile = pile[pile[:, 0].argsort()]
        # no memory cache
        rows = self.queryset.values_list(*self.all_fields).iterator()
        # here is where slow evaluation happens
        arrays = [np.array(col) for col in zip(*rows)]
        self.named_arrays = dict(zip(fields, arrays))
    """

    def set_arrays(self):
        # if queryset is not completely empty
        if self.queryset.exists():
            rows = self.queryset.values_list(*self.all_fields)
            sorted_rows = sorted(rows, key=lambda row: row[0])
            columns = zip(*sorted_rows)
            self.arrays = []
            for col in columns:
                contains_sequence = any(isinstance(value, (list, tuple, np.ndarray)) for value in col)
                if contains_sequence:
                    self.arrays.append(np.array(col, dtype=object))
                else:
                    self.arrays.append(np.array(col))

    def get_array_len(self):
        if self.arrays is not None:
            return self.arrays[0].shape[0]

    def get_full_time_array(self):
        if self.arrays is not None:
            return self.arrays[0]

    def set_bin_map(self, bin_starts_array):
        self.bin_map = np.searchsorted(bin_starts_array, self.get_full_time_array(), side="right")


class Bin():

    # points per plot: since plot aggregation is dynamic, either need to have fixed bin sizes or points per plot
    PPP = 1000

    def __init__(self, t_start, t_stop):

        timedelta = t_stop - t_start 
        self.bin_seconds = math.ceil(timedelta.total_seconds() / self.PPP)
        self.bin_td = dt.timedelta(seconds=self.bin_seconds)
        self.half_bin = math.ceil(self.bin_seconds / 2)

    def t_next(self, t_current):
        #print(f"in t_next : {t_current}, {t_current + self.bin_td}")
        return t_current + self.bin_td

    def t_previous(self, t_current):
        #print(f"in t_prev : {t_current}, {t_current - self.bin_td}")
        return t_current - self.bin_td



class Plot():

    # start and stop as datetimes
    t_start = None
    t_stop = None
    
    # in seconds
    bin_instance = None
    # numpy range of the starts of time bins
    bin_starts_array = None
    bin_centers_array = None

    # plotly figure
    figure = None

    def __init__(self, t_start, t_stop, variable, x_field, validate):

        # start and stop as datetimes
        self.t_start = t_start
        self.t_stop = t_stop

        # instances of var
        self.variable = variable
      
        # Flag to show if validation will be applied
        self.validate = validate

        # Flag to now if aggregation happened
        self.aggregation = None

        # block for aggregation
        self.bin_instance = None
        # numpy range of the starts of time bins
        self.bin_starts_array = None
        self.bin_centers_array = None

        # name of x_field
        self.x_field = x_field
        # array of timestamps for plot points
        self.x_field_array = None

        # numpy datatype
        self.y_field_numpy_type = variable.get_numpy_data_type()
        # names of y_fields
        self.y_fields = list(variable.dynamic.order_by('multipart_index').values_list('field_name', flat=True))
        # a list of field arrays, in the same order as y_fields
        self.y_arrays = []
        self.y_axis_array = None
        self.z_array = None
        
        self.invalid_values = []
        
        self.figure = None



    def prepare_bins(self, bin_instance):
        i_start = ti(self.t_start)
        i_stop = ti(self.t_stop)
        self.bin_instance = bin_instance
        # *2 here because right limit in arange is non-inclusive, 
        # but a little data in the query could be left beyond last bin, since bin size is rounded
        self.bin_starts_array = np.arange(
                i_start,
                i_stop + (bin_instance.bin_seconds*2),
                step=bin_instance.bin_seconds)
        self.bin_centers_array = self.bin_starts_array + bin_instance.half_bin
    
    # index that marks values beyond validmin - valimax interval
    def validation_index(self, arr, field_index=None):
        condition = False
        
        if self.variable.validmin is not None:
            #print(type(self.variable.validmin))
          
            if field_index is not None and isinstance(self.variable.validmin, list):
                validmin = self.variable.validmin[field_index]
            else:
                validmin = self.variable.validmin
            validmin_value = DataType.proper_type(validmin, arr[0])
           
            condition = condition | (arr < validmin_value)

        if self.variable.validmax is not None:
            if field_index is not None and isinstance(self.variable.validmax, list):
                validmax = self.variable.validmax[field_index]
            else:
                validmax = self.variable.validmax
            validmax_value = DataType.proper_type(validmax, arr[0])
           
            condition = condition | (arr > validmax_value)
    
        # can not just swap values here, because for int type there is no nan alternative

        if isinstance(condition, np.ndarray):
            self.invalid_values.append(f"{int(condition.sum())} / {condition.shape[0]} [{validmin}, {validmax}]")
        else:
            condition = None
            self.invalid_values.append("no validmin/validmax")
        
        if self.validate:
            return condition
        else:
            return None

    def validate_spectrogram(self):
        if not self.validate:
            return

        if self.z_array is None or not isinstance(self.z_array, np.ndarray) or self.z_array.size == 0:
            return

        z = self.z_array
        finite_mask = np.isfinite(z)

        sample = 0.0
        try:
            finite_idx = np.flatnonzero(finite_mask)
            if finite_idx.size > 0:
                sample = float(z.flat[int(finite_idx[0])])
        except Exception:
            sample = 0.0

        invalid_mask = np.zeros(z.shape, dtype=bool)
        total = int(z.size)
        counts = {
            "nonfinite": int((~finite_mask).sum()),
            "fill": 0,
            "lt_min": 0,
            "gt_max": 0,
        }

        if getattr(self.variable, "fillval", None) is not None:
            try:
                fill_value = DataType.proper_type(self.variable.fillval, sample)
            except Exception:
                fill_value = None
            if fill_value is not None and not isinstance(fill_value, (list, tuple, np.ndarray, dict)):
                fill_mask = finite_mask & (z == float(fill_value))
                counts["fill"] = int(fill_mask.sum())
                invalid_mask |= fill_mask

        width = z.shape[1] if z.ndim == 2 else None
        raw_validmin = getattr(self.variable, "validmin", None)
        raw_validmax = getattr(self.variable, "validmax", None)

        def parse_bound(raw):
            if raw is None:
                return None
            try:
                return DataType.proper_type(raw, sample)
            except Exception:
                return None

        vmin_display = raw_validmin
        vmax_display = raw_validmax

        if isinstance(raw_validmin, list) and width is not None and len(raw_validmin) == width:
            vmins = [parse_bound(v) for v in raw_validmin]
            vmins = np.array([float(v) if v is not None else np.nan for v in vmins], dtype=float)
            lt_mask = finite_mask & (z < vmins)
            counts["lt_min"] = int(lt_mask.sum())
            invalid_mask |= lt_mask
            vmin_display = f"list(len={len(vmins)})"
        else:
            vmin = parse_bound(raw_validmin)
            if vmin is not None and not isinstance(vmin, (list, tuple, np.ndarray, dict)):
                lt_mask = finite_mask & (z < float(vmin))
                counts["lt_min"] = int(lt_mask.sum())
                invalid_mask |= lt_mask
                vmin_display = vmin

        if isinstance(raw_validmax, list) and width is not None and len(raw_validmax) == width:
            vmaxs = [parse_bound(v) for v in raw_validmax]
            vmaxs = np.array([float(v) if v is not None else np.nan for v in vmaxs], dtype=float)
            gt_mask = finite_mask & (z > vmaxs)
            counts["gt_max"] = int(gt_mask.sum())
            invalid_mask |= gt_mask
            vmax_display = f"list(len={len(vmaxs)})"
        else:
            vmax = parse_bound(raw_validmax)
            if vmax is not None and not isinstance(vmax, (list, tuple, np.ndarray, dict)):
                gt_mask = finite_mask & (z > float(vmax))
                counts["gt_max"] = int(gt_mask.sum())
                invalid_mask |= gt_mask
                vmax_display = vmax

        invalid_count = int(invalid_mask.sum())
        self.invalid_values.append(
            (
                f"spectrogram validate: invalid={invalid_count}/{total}, "
                f"nonfinite={counts['nonfinite']}, fill={counts['fill']}, "
                f"<min={counts['lt_min']}, >max={counts['gt_max']}, "
                f"validmin={vmin_display}, validmax={vmax_display}"
            )
        )

        if invalid_count:
            z[invalid_mask] = np.nan


    def get_x_array(self, query):
        self.x_field_array = np.array(list(map(it, query.get_full_time_array())))

    def get_y_arrays(self, query):
        for field in self.y_fields:
            field_index = query.all_fields.index(field)
            full_value_array = query.arrays[field_index]
            
            # only nan values for this variable
            if np.isnan(full_value_array).all():
                self.y_arrays.append([])
            else:
                self.y_arrays.append(full_value_array.astype(self.y_field_numpy_type))

        # applying validation index in case of no aggregation is a little harder:
        # the only way to skip values when plotting is skipping index in both x_array and y_array at the same index
        # but there is a single x array and y arrays could have different validation indexes so i have to have multiple x_arrays or apply aggregation when plotting
        # chose the second option

    def get_spectrogram_arrays(self, query):
        self.get_x_array(query)

        if len(self.y_fields) == 0:
            self.z_array = np.array([])
            self.y_axis_array = np.array([])
            return

        z_field = self.y_fields[0]
        z_index = query.all_fields.index(z_field)
        z_source = query.arrays[z_index]

        dep1_values = None
        if self.variable.depend_1 is not None:
            depend_var = self.variable.dataset.variables.get_or_none(name=self.variable.depend_1)
            if depend_var is not None and depend_var.dynamic.exists():
                depend_fields = list(depend_var.dynamic.order_by('multipart_index').values_list('field_name', flat=True))
                present_depend_fields = [field_name for field_name in depend_fields if field_name in query.all_fields]
                if len(present_depend_fields) == 1:
                    dep1_values = query.arrays[query.all_fields.index(present_depend_fields[0])]
                elif len(present_depend_fields) > 1:
                    try:
                        dep1_values = np.array(
                            [query.arrays[query.all_fields.index(field_name)][0] for field_name in present_depend_fields],
                            dtype=float,
                        )
                    except Exception:
                        dep1_values = None

        y_axis = None
        if dep1_values is not None:
            if isinstance(dep1_values, np.ndarray) and dep1_values.ndim == 1 and dep1_values.size > 1:
                if not isinstance(dep1_values[0], (list, tuple, np.ndarray)):
                    y_axis = dep1_values.astype(float)

            if y_axis is None:
                for value in dep1_values:
                    if isinstance(value, (list, tuple, np.ndarray)) and len(value) > 0:
                        y_axis = np.array(value, dtype=float)
                        break

        rows = []
        inferred_width = len(y_axis) if y_axis is not None else None

        for value in z_source:
            if isinstance(value, (list, tuple, np.ndarray)):
                row = np.array(value, dtype=float)
            else:
                row = np.array([], dtype=float)

            if inferred_width is None and row.size > 0:
                inferred_width = row.size

            rows.append(row)

        if inferred_width is None:
            self.z_array = np.array([])
            self.y_axis_array = np.array([])
            return

        normalized_rows = []
        for row in rows:
            if row.size == inferred_width:
                normalized_rows.append(row)
            elif row.size == 0:
                normalized_rows.append(np.full(inferred_width, np.nan))
            elif row.size < inferred_width:
                padded = np.full(inferred_width, np.nan)
                padded[:row.size] = row
                normalized_rows.append(padded)
            else:
                normalized_rows.append(row[:inferred_width])

        self.z_array = np.vstack(normalized_rows) if len(normalized_rows) > 0 else np.array([])
        if y_axis is None:
            self.y_axis_array = np.arange(inferred_width)
        else:
            self.y_axis_array = y_axis
        self.validate_spectrogram()

    def get_agg_x_array(self):
        self.x_field_array = np.array(list(map(it, self.bin_centers_array)))

    # definitely could reduce # of steps here
    def get_agg_y_arrays(self, query):
        
        for i, field in enumerate(self.y_fields):
            field_index = query.all_fields.index(field)
            full_value_array = query.arrays[field_index]

            # getting an index of nans in value array
            mask = ~np.isnan(full_value_array)
           
            # getting an index of invalid values
            validation_index = self.validation_index(full_value_array, field_index=i)
            # if index exists and there is at least one invalid value, combine it with the mask
            if validation_index is not None and validation_index.any():
                mask = mask & ~validation_index

            
            # getting maps for only non-nans
            val_bin_map = query.bin_map[mask]
            # getting only non-nans
            val_array = full_value_array[mask]

            idx, pos, counts = np.unique(val_bin_map, return_index=True, return_counts=True)

            # number of groups even left
            # if no aggregation groups survived - that means there will be no points on the plot
            if idx.shape[0] == 0:
                print(f"no data in field {field}, out of {self.variable.name} {self.variable.dataset}")
                self.y_arrays.append([])
                continue

            # getting sums for groups
            sums = np.add.reduceat(val_array, pos, axis=0)
            # getting values
            means = sums / counts
            # reconstructing index
            np_type = self.y_field_numpy_type if self.y_field_numpy_type is not None else means.dtype
            # get an array of nans of size and type
            result = np.full(self.x_field_array.shape, np.nan, np_type)
            # fill in significant values
            result[idx] = means
            self.y_arrays.append(result)
        
    def set_arrays(self, query):
        if self.variable.display_type == "spectrogram":
            self.get_spectrogram_arrays(query)
            return

        # includes validation
        if self.aggregation:
            self.get_agg_x_array()
            self.get_agg_y_arrays(query)

        # validation on plotting, because no nans for int types means no swap
        else:
            self.get_x_array(query)
            self.get_y_arrays(query)

    # returns a pair of x_array and y_array for each plot
    def get_values(self, index):
        if self.aggregation:
            return self.x_field_array, self.y_arrays[index]
        else:
            # apply validation here instead:
            validation_index = self.validation_index(self.y_arrays[index], field_index=index)
            if validation_index is not None and validation_index.any():
                return self.x_field_array[~validation_index], self.y_arrays[index][~validation_index]
            else:
                return self.x_field_array, self.y_arrays[index]
    


    def get_figure(self):
        if self.variable.display_type == "spectrogram":
            self.figure = spectrogram(self)
            return

        if len(self.y_fields) == 1:
            self.figure = scatter(self)
        else:
            self.figure = n_trace(self)
