from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid
from solarterra.abstract_models import GetManager
from load_cdf.models import CDFFileStored, Float32Field

class WIND_WI_H0_MFI_v01_data(models.Model):

	
	brmsgsm_by_rms = Float32Field(blank=True, null=True)
	
	pgse_x = Float32Field(blank=True, null=True)
	
	pgse_y = Float32Field(blank=True, null=True)
	
	pgse_z = Float32Field(blank=True, null=True)
	
	tiltang_part_1 = Float32Field(blank=True, null=True)
	
	epoch3_part_1 = models.BigIntegerField(blank=True, null=True)
	
	b3gse_bx = Float32Field(blank=True, null=True)
	
	b3gse_by = Float32Field(blank=True, null=True)
	
	b3gse_bz = Float32Field(blank=True, null=True)
	
	num1_pts_part_1 = models.IntegerField(blank=True, null=True)
	
	b1rmsgsm_bx_rms = Float32Field(blank=True, null=True)
	
	b1rmsgsm_bz_rms = Float32Field(blank=True, null=True)
	
	p1gse_x = Float32Field(blank=True, null=True)
	
	p1gse_y = Float32Field(blank=True, null=True)
	
	p1gse_z = Float32Field(blank=True, null=True)
	
	bgsm_bx = Float32Field(blank=True, null=True)
	
	epoch_part_1 = models.BigIntegerField(blank=True, null=True)
	
	time_pb5_year = models.IntegerField(blank=True, null=True)
	
	time_pb5_day_of_year = models.IntegerField(blank=True, null=True)
	
	time_pb5_elapsed_milliseconds_of_day = models.IntegerField(blank=True, null=True)
	
	num_pts_part_1 = models.IntegerField(blank=True, null=True)
	
	bf1_part_1 = Float32Field(blank=True, null=True)
	
	brmsf1_part_1 = Float32Field(blank=True, null=True)
	
	brmsgsm_bx_rms = Float32Field(blank=True, null=True)
	
	brmsgsm_bz_rms = Float32Field(blank=True, null=True)
	
	num3_pts_part_1 = models.IntegerField(blank=True, null=True)
	
	b1rmsgsm_by_rms = Float32Field(blank=True, null=True)
	
	bgsm_by = Float32Field(blank=True, null=True)
	
	bgsm_bz = Float32Field(blank=True, null=True)
	
	bgse_bx = Float32Field(blank=True, null=True)
	
	bgse_by = Float32Field(blank=True, null=True)
	
	bgse_bz = Float32Field(blank=True, null=True)
	
	brmsgse_bx_rms = Float32Field(blank=True, null=True)
	
	brmsgse_by_rms = Float32Field(blank=True, null=True)
	
	brmsgse_bz_rms = Float32Field(blank=True, null=True)
	
	dist_part_1 = Float32Field(blank=True, null=True)
	
	pgsm_x = Float32Field(blank=True, null=True)
	
	pgsm_y = Float32Field(blank=True, null=True)
	
	pgsm_z = Float32Field(blank=True, null=True)
	
	sgsm_unit_vector_x = Float32Field(blank=True, null=True)
	
	sgsm_unit_vector_y = Float32Field(blank=True, null=True)
	
	sgsm_unit_vector_z = Float32Field(blank=True, null=True)
	
	sgse_unit_vector_x = Float32Field(blank=True, null=True)
	
	db_sc_bx = Float32Field(blank=True, null=True)
	
	db_sc_by = Float32Field(blank=True, null=True)
	
	db_sc_bz = Float32Field(blank=True, null=True)
	
	range_o_part_1 = Float32Field(blank=True, null=True)
	
	spc_mode_part_1 = models.IntegerField(blank=True, null=True)
	
	mag_mode_part_1 = models.IntegerField(blank=True, null=True)
	
	time3_pb5_year = models.IntegerField(blank=True, null=True)
	
	time3_pb5_elapsed_milliseconds_of_day = models.IntegerField(blank=True, null=True)
	
	b3f1_part_1 = Float32Field(blank=True, null=True)
	
	b3rmsf1_part_1 = Float32Field(blank=True, null=True)
	
	b3gsm_bx = Float32Field(blank=True, null=True)
	
	b3gsm_by = Float32Field(blank=True, null=True)
	
	b3gsm_bz = Float32Field(blank=True, null=True)
	
	b3rmsgsm_by_rms = Float32Field(blank=True, null=True)
	
	b3rmsgsm_bz_rms = Float32Field(blank=True, null=True)
	
	b3rmsgse_bx_rms = Float32Field(blank=True, null=True)
	
	b3rmsgse_by_rms = Float32Field(blank=True, null=True)
	
	b3rmsgse_bz_rms = Float32Field(blank=True, null=True)
	
	time1_pb5_year = models.IntegerField(blank=True, null=True)
	
	time1_pb5_day_of_year = models.IntegerField(blank=True, null=True)
	
	time1_pb5_elapsed_milliseconds_of_day = models.IntegerField(blank=True, null=True)
	
	b1f1_part_1 = Float32Field(blank=True, null=True)
	
	b1rmsf1_part_1 = Float32Field(blank=True, null=True)
	
	b1gsm_bx = Float32Field(blank=True, null=True)
	
	b1gsm_bz = Float32Field(blank=True, null=True)
	
	b1gse_bx = Float32Field(blank=True, null=True)
	
	b1gse_by = Float32Field(blank=True, null=True)
	
	b1gse_bz = Float32Field(blank=True, null=True)
	
	b1rmsgse_by_rms = Float32Field(blank=True, null=True)
	
	b1rmsgse_bz_rms = Float32Field(blank=True, null=True)
	
	dist1_part_1 = Float32Field(blank=True, null=True)
	
	p1gsm_x = Float32Field(blank=True, null=True)
	
	p1gsm_y = Float32Field(blank=True, null=True)
	
	p1gsm_z = Float32Field(blank=True, null=True)
	
	s1gsm_unit_vector_y = Float32Field(blank=True, null=True)
	
	s1gsm_unit_vector_z = Float32Field(blank=True, null=True)
	
	s1gse_unit_vector_x = Float32Field(blank=True, null=True)
	
	range_i_part_1 = Float32Field(blank=True, null=True)
	
	time3_pb5_day_of_year = models.IntegerField(blank=True, null=True)
	
	b3rmsgsm_bx_rms = Float32Field(blank=True, null=True)
	
	epoch1_part_1 = models.BigIntegerField(blank=True, null=True)
	
	b1gsm_by = Float32Field(blank=True, null=True)
	
	b1rmsgse_bx_rms = Float32Field(blank=True, null=True)
	
	s1gsm_unit_vector_x = Float32Field(blank=True, null=True)
	
	
	cdf_file = models.ForeignKey(CDFFileStored, on_delete=models.SET_NULL, related_name="WIND_WI_H0_MFI_v01_data_data", db_index=False, blank=True, null=True)

	objects = GetManager()	
