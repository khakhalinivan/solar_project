from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid
from solarterra.abstract_models import GetManager
from load_cdf.models import CDFFileStored, Float32Field

class WIND_WI_K0_SWE_v01_data(models.Model):

	
	epoch = models.BigIntegerField(blank=True, null=True)
	
	delta_time = models.FloatField(blank=True, null=True)
	
	time_pb5_year = models.IntegerField(blank=True, null=True)
	
	time_pb5_day_of_year = models.IntegerField(blank=True, null=True)
	
	time_pb5_elapsed_millisecond_of_day = models.IntegerField(blank=True, null=True)
	
	gap_flag = models.IntegerField(blank=True, null=True)
	
	mode = models.IntegerField(blank=True, null=True)
	
	sc_pos_gse_x = Float32Field(blank=True, null=True)
	
	sc_pos_gse_y = Float32Field(blank=True, null=True)
	
	sc_pos_gse_z = Float32Field(blank=True, null=True)
	
	sc_pos_gsm_x = Float32Field(blank=True, null=True)
	
	sc_pos_gsm_y = Float32Field(blank=True, null=True)
	
	sc_pos_gsm_z = Float32Field(blank=True, null=True)
	
	sc_pos_r = Float32Field(blank=True, null=True)
	
	dqf = models.IntegerField(blank=True, null=True)
	
	qf_v = models.IntegerField(blank=True, null=True)
	
	qf_vth = models.IntegerField(blank=True, null=True)
	
	thermal_spd = Float32Field(blank=True, null=True)
	
	np = Float32Field(blank=True, null=True)
	
	alpha_percent = Float32Field(blank=True, null=True)
	
	qf_np = models.IntegerField(blank=True, null=True)
	
	qf_ap = models.IntegerField(blank=True, null=True)
	
	v_gse_vx = Float32Field(blank=True, null=True)
	
	v_gse_vy = Float32Field(blank=True, null=True)
	
	v_gse_vz = Float32Field(blank=True, null=True)
	
	v_gsm_vx = Float32Field(blank=True, null=True)
	
	v_gsm_vy = Float32Field(blank=True, null=True)
	
	v_gsm_vz = Float32Field(blank=True, null=True)
	
	v_gse_p_flow_speed = Float32Field(blank=True, null=True)
	
	v_gse_p_ew_flow = Float32Field(blank=True, null=True)
	
	v_gse_p_ns_flow = Float32Field(blank=True, null=True)
	
	
	cdf_file = models.ForeignKey(CDFFileStored, on_delete=models.SET_NULL, related_name="WIND_WI_K0_SWE_v01_data_data", db_index=False, blank=True, null=True)

	objects = GetManager()	
