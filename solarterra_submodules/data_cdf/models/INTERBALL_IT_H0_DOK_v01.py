from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid
from solarterra.abstract_models import GetManager
from load_cdf.models import CDFFileStored, Float32Field

class INTERBALL_IT_H0_DOK_v01_data(models.Model):

	
	epoch_3 = models.BigIntegerField(blank=True, null=True)
	
	epoch_4 = models.BigIntegerField(blank=True, null=True)
	
	time_pb5_1_part_1 = models.IntegerField(blank=True, null=True)
	
	time_pb5_1_part_2 = models.IntegerField(blank=True, null=True)
	
	time_pb5_2_part_1 = models.IntegerField(blank=True, null=True)
	
	time_pb5_2_part_2 = models.IntegerField(blank=True, null=True)
	
	time_pb5_2_part_3 = models.IntegerField(blank=True, null=True)
	
	time_pb5_3_part_1 = models.IntegerField(blank=True, null=True)
	
	time_pb5_3_part_2 = models.IntegerField(blank=True, null=True)
	
	time_pb5_4_part_1 = models.IntegerField(blank=True, null=True)
	
	time_pb5_4_part_2 = models.IntegerField(blank=True, null=True)
	
	time_pb5_4_part_3 = models.IntegerField(blank=True, null=True)
	
	fmode_1 = models.PositiveIntegerField(blank=True, null=True)
	
	fmode_2 = models.PositiveIntegerField(blank=True, null=True)
	
	fmode_3 = models.PositiveIntegerField(blank=True, null=True)
	
	dtime_1 = Float32Field(blank=True, null=True)
	
	dtime_2 = Float32Field(blank=True, null=True)
	
	dtime_3 = Float32Field(blank=True, null=True)
	
	dtime_4 = Float32Field(blank=True, null=True)
	
	a_theta_4 = Float32Field(blank=True, null=True)
	
	se_1 = ArrayField(Float32Field(blank=True, null=True), blank=True, null=True)
	
	se_2 = ArrayField(Float32Field(blank=True, null=True), blank=True, null=True)
	
	si_3 = ArrayField(Float32Field(blank=True, null=True), blank=True, null=True)
	
	si_4 = ArrayField(Float32Field(blank=True, null=True), blank=True, null=True)
	
	label_e_1_part_2 = models.TextField(blank=True, null=True)
	
	label_e_1_part_3 = models.TextField(blank=True, null=True)
	
	label_e_1_part_4 = models.TextField(blank=True, null=True)
	
	label_e_1_part_5 = models.TextField(blank=True, null=True)
	
	label_e_1_part_6 = models.TextField(blank=True, null=True)
	
	label_e_1_part_8 = models.TextField(blank=True, null=True)
	
	label_e_1_part_9 = models.TextField(blank=True, null=True)
	
	label_e_1_part_10 = models.TextField(blank=True, null=True)
	
	label_e_1_part_11 = models.TextField(blank=True, null=True)
	
	label_e_1_part_12 = models.TextField(blank=True, null=True)
	
	label_e_1_part_14 = models.TextField(blank=True, null=True)
	
	label_e_1_part_15 = models.TextField(blank=True, null=True)
	
	label_e_1_part_16 = models.TextField(blank=True, null=True)
	
	label_e_1_part_17 = models.TextField(blank=True, null=True)
	
	label_e_1_part_18 = models.TextField(blank=True, null=True)
	
	label_e_1_part_20 = models.TextField(blank=True, null=True)
	
	label_e_1_part_21 = models.TextField(blank=True, null=True)
	
	label_e_1_part_22 = models.TextField(blank=True, null=True)
	
	label_e_1_part_23 = models.TextField(blank=True, null=True)
	
	label_e_1_part_24 = models.TextField(blank=True, null=True)
	
	label_e_1_part_26 = models.TextField(blank=True, null=True)
	
	label_e_1_part_27 = models.TextField(blank=True, null=True)
	
	label_e_1_part_28 = models.TextField(blank=True, null=True)
	
	label_e_1_part_29 = models.TextField(blank=True, null=True)
	
	label_e_1_part_30 = models.TextField(blank=True, null=True)
	
	label_e_1_part_31 = models.TextField(blank=True, null=True)
	
	label_e_1_part_33 = models.TextField(blank=True, null=True)
	
	label_e_1_part_34 = models.TextField(blank=True, null=True)
	
	label_e_1_part_35 = models.TextField(blank=True, null=True)
	
	label_e_1_part_36 = models.TextField(blank=True, null=True)
	
	label_e_1_part_37 = models.TextField(blank=True, null=True)
	
	label_e_1_part_39 = models.TextField(blank=True, null=True)
	
	label_e_1_part_40 = models.TextField(blank=True, null=True)
	
	label_e_1_part_41 = models.TextField(blank=True, null=True)
	
	label_e_1_part_42 = models.TextField(blank=True, null=True)
	
	label_e_1_part_43 = models.TextField(blank=True, null=True)
	
	label_e_1_part_45 = models.TextField(blank=True, null=True)
	
	label_e_1_part_46 = models.TextField(blank=True, null=True)
	
	label_e_1_part_47 = models.TextField(blank=True, null=True)
	
	label_e_1_part_48 = models.TextField(blank=True, null=True)
	
	label_e_1_part_50 = models.TextField(blank=True, null=True)
	
	label_e_1_part_51 = models.TextField(blank=True, null=True)
	
	label_e_1_part_52 = models.TextField(blank=True, null=True)
	
	label_e_1_part_54 = models.TextField(blank=True, null=True)
	
	label_e_1_part_55 = models.TextField(blank=True, null=True)
	
	label_e_2_part_1 = models.TextField(blank=True, null=True)
	
	label_e_2_part_2 = models.TextField(blank=True, null=True)
	
	label_e_2_part_3 = models.TextField(blank=True, null=True)
	
	label_e_2_part_5 = models.TextField(blank=True, null=True)
	
	label_e_2_part_6 = models.TextField(blank=True, null=True)
	
	label_e_2_part_7 = models.TextField(blank=True, null=True)
	
	label_e_2_part_8 = models.TextField(blank=True, null=True)
	
	label_e_2_part_9 = models.TextField(blank=True, null=True)
	
	label_e_2_part_11 = models.TextField(blank=True, null=True)
	
	label_e_2_part_12 = models.TextField(blank=True, null=True)
	
	label_e_2_part_13 = models.TextField(blank=True, null=True)
	
	label_e_2_part_14 = models.TextField(blank=True, null=True)
	
	label_e_2_part_15 = models.TextField(blank=True, null=True)
	
	label_e_2_part_16 = models.TextField(blank=True, null=True)
	
	label_e_2_part_18 = models.TextField(blank=True, null=True)
	
	label_e_2_part_19 = models.TextField(blank=True, null=True)
	
	label_e_2_part_20 = models.TextField(blank=True, null=True)
	
	label_e_2_part_21 = models.TextField(blank=True, null=True)
	
	label_e_2_part_22 = models.TextField(blank=True, null=True)
	
	label_e_2_part_24 = models.TextField(blank=True, null=True)
	
	label_e_2_part_25 = models.TextField(blank=True, null=True)
	
	label_e_2_part_26 = models.TextField(blank=True, null=True)
	
	label_e_2_part_27 = models.TextField(blank=True, null=True)
	
	label_e_2_part_28 = models.TextField(blank=True, null=True)
	
	label_e_2_part_30 = models.TextField(blank=True, null=True)
	
	label_e_2_part_31 = models.TextField(blank=True, null=True)
	
	label_e_2_part_32 = models.TextField(blank=True, null=True)
	
	label_e_2_part_33 = models.TextField(blank=True, null=True)
	
	label_e_2_part_34 = models.TextField(blank=True, null=True)
	
	label_e_2_part_36 = models.TextField(blank=True, null=True)
	
	label_e_2_part_37 = models.TextField(blank=True, null=True)
	
	label_e_2_part_38 = models.TextField(blank=True, null=True)
	
	label_e_2_part_39 = models.TextField(blank=True, null=True)
	
	label_e_2_part_40 = models.TextField(blank=True, null=True)
	
	label_e_2_part_42 = models.TextField(blank=True, null=True)
	
	label_e_2_part_43 = models.TextField(blank=True, null=True)
	
	label_e_2_part_44 = models.TextField(blank=True, null=True)
	
	label_e_2_part_45 = models.TextField(blank=True, null=True)
	
	label_e_2_part_46 = models.TextField(blank=True, null=True)
	
	label_e_2_part_47 = models.TextField(blank=True, null=True)
	
	label_e_2_part_49 = models.TextField(blank=True, null=True)
	
	label_e_2_part_50 = models.TextField(blank=True, null=True)
	
	label_e_2_part_51 = models.TextField(blank=True, null=True)
	
	label_e_2_part_52 = models.TextField(blank=True, null=True)
	
	label_e_2_part_53 = models.TextField(blank=True, null=True)
	
	label_e_2_part_55 = models.TextField(blank=True, null=True)
	
	label_e_3_part_1 = models.TextField(blank=True, null=True)
	
	label_e_3_part_2 = models.TextField(blank=True, null=True)
	
	label_e_3_part_3 = models.TextField(blank=True, null=True)
	
	label_e_3_part_4 = models.TextField(blank=True, null=True)
	
	label_e_3_part_6 = models.TextField(blank=True, null=True)
	
	label_e_3_part_7 = models.TextField(blank=True, null=True)
	
	label_e_3_part_8 = models.TextField(blank=True, null=True)
	
	label_e_3_part_9 = models.TextField(blank=True, null=True)
	
	label_e_3_part_10 = models.TextField(blank=True, null=True)
	
	label_e_3_part_12 = models.TextField(blank=True, null=True)
	
	label_e_3_part_13 = models.TextField(blank=True, null=True)
	
	label_e_3_part_15 = models.TextField(blank=True, null=True)
	
	label_e_3_part_16 = models.TextField(blank=True, null=True)
	
	label_e_3_part_17 = models.TextField(blank=True, null=True)
	
	label_e_3_part_19 = models.TextField(blank=True, null=True)
	
	label_e_3_part_20 = models.TextField(blank=True, null=True)
	
	label_e_3_part_21 = models.TextField(blank=True, null=True)
	
	label_e_3_part_22 = models.TextField(blank=True, null=True)
	
	label_e_3_part_23 = models.TextField(blank=True, null=True)
	
	label_e_3_part_25 = models.TextField(blank=True, null=True)
	
	label_e_3_part_26 = models.TextField(blank=True, null=True)
	
	label_e_3_part_27 = models.TextField(blank=True, null=True)
	
	label_e_3_part_28 = models.TextField(blank=True, null=True)
	
	label_e_3_part_29 = models.TextField(blank=True, null=True)
	
	label_e_3_part_31 = models.TextField(blank=True, null=True)
	
	label_e_3_part_32 = models.TextField(blank=True, null=True)
	
	label_e_3_part_33 = models.TextField(blank=True, null=True)
	
	label_e_3_part_34 = models.TextField(blank=True, null=True)
	
	label_e_3_part_35 = models.TextField(blank=True, null=True)
	
	label_e_3_part_36 = models.TextField(blank=True, null=True)
	
	label_e_3_part_38 = models.TextField(blank=True, null=True)
	
	label_e_3_part_39 = models.TextField(blank=True, null=True)
	
	label_e_3_part_40 = models.TextField(blank=True, null=True)
	
	label_e_3_part_41 = models.TextField(blank=True, null=True)
	
	label_e_3_part_42 = models.TextField(blank=True, null=True)
	
	label_e_3_part_44 = models.TextField(blank=True, null=True)
	
	label_e_3_part_45 = models.TextField(blank=True, null=True)
	
	label_e_3_part_46 = models.TextField(blank=True, null=True)
	
	label_e_3_part_47 = models.TextField(blank=True, null=True)
	
	label_e_3_part_48 = models.TextField(blank=True, null=True)
	
	label_e_3_part_50 = models.TextField(blank=True, null=True)
	
	label_e_3_part_51 = models.TextField(blank=True, null=True)
	
	label_e_3_part_52 = models.TextField(blank=True, null=True)
	
	label_e_3_part_53 = models.TextField(blank=True, null=True)
	
	label_e_3_part_54 = models.TextField(blank=True, null=True)
	
	label_e_3_part_56 = models.TextField(blank=True, null=True)
	
	label_e_4_part_1 = models.TextField(blank=True, null=True)
	
	label_e_4_part_2 = models.TextField(blank=True, null=True)
	
	label_e_4_part_3 = models.TextField(blank=True, null=True)
	
	label_e_4_part_4 = models.TextField(blank=True, null=True)
	
	label_e_4_part_6 = models.TextField(blank=True, null=True)
	
	label_e_4_part_7 = models.TextField(blank=True, null=True)
	
	label_e_4_part_8 = models.TextField(blank=True, null=True)
	
	label_e_4_part_9 = models.TextField(blank=True, null=True)
	
	label_e_4_part_10 = models.TextField(blank=True, null=True)
	
	label_e_4_part_11 = models.TextField(blank=True, null=True)
	
	label_e_4_part_13 = models.TextField(blank=True, null=True)
	
	label_e_4_part_14 = models.TextField(blank=True, null=True)
	
	label_e_4_part_15 = models.TextField(blank=True, null=True)
	
	label_e_4_part_16 = models.TextField(blank=True, null=True)
	
	label_e_4_part_17 = models.TextField(blank=True, null=True)
	
	label_e_4_part_19 = models.TextField(blank=True, null=True)
	
	label_e_4_part_20 = models.TextField(blank=True, null=True)
	
	label_e_4_part_21 = models.TextField(blank=True, null=True)
	
	label_e_4_part_22 = models.TextField(blank=True, null=True)
	
	label_e_4_part_23 = models.TextField(blank=True, null=True)
	
	label_e_4_part_25 = models.TextField(blank=True, null=True)
	
	label_e_4_part_26 = models.TextField(blank=True, null=True)
	
	label_e_4_part_27 = models.TextField(blank=True, null=True)
	
	label_e_4_part_28 = models.TextField(blank=True, null=True)
	
	label_e_4_part_29 = models.TextField(blank=True, null=True)
	
	label_e_4_part_31 = models.TextField(blank=True, null=True)
	
	label_e_4_part_32 = models.TextField(blank=True, null=True)
	
	label_e_4_part_34 = models.TextField(blank=True, null=True)
	
	label_e_4_part_35 = models.TextField(blank=True, null=True)
	
	label_e_4_part_36 = models.TextField(blank=True, null=True)
	
	label_e_4_part_38 = models.TextField(blank=True, null=True)
	
	label_e_4_part_39 = models.TextField(blank=True, null=True)
	
	label_e_4_part_40 = models.TextField(blank=True, null=True)
	
	label_e_4_part_41 = models.TextField(blank=True, null=True)
	
	label_e_4_part_42 = models.TextField(blank=True, null=True)
	
	label_e_4_part_44 = models.TextField(blank=True, null=True)
	
	label_e_4_part_45 = models.TextField(blank=True, null=True)
	
	label_e_4_part_46 = models.TextField(blank=True, null=True)
	
	label_e_4_part_47 = models.TextField(blank=True, null=True)
	
	label_e_4_part_48 = models.TextField(blank=True, null=True)
	
	label_e_4_part_50 = models.TextField(blank=True, null=True)
	
	label_e_4_part_51 = models.TextField(blank=True, null=True)
	
	label_e_4_part_52 = models.TextField(blank=True, null=True)
	
	label_e_4_part_53 = models.TextField(blank=True, null=True)
	
	label_e_4_part_54 = models.TextField(blank=True, null=True)
	
	label_e_4_part_55 = models.TextField(blank=True, null=True)
	
	ener_e_1_part_1 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_2 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_3 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_4 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_5 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_7 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_8 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_9 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_10 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_11 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_13 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_14 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_15 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_16 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_17 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_19 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_20 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_21 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_22 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_23 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_25 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_26 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_27 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_28 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_29 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_30 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_32 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_33 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_34 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_35 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_36 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_38 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_39 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_40 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_41 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_42 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_44 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_45 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_46 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_47 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_48 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_50 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_51 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_53 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_54 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_55 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_2 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_3 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_4 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_5 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_6 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_7 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_9 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_10 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_11 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_12 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_13 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_15 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_16 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_17 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_18 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_19 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_21 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_22 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_23 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_24 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_25 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_27 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_28 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_29 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_30 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_31 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_33 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_34 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_35 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_36 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_37 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_38 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_40 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_41 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_42 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_43 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_44 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_46 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_47 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_48 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_49 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_50 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_52 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_53 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_54 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_55 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_56 = Float32Field(blank=True, null=True)
	
	gap_flag_3 = models.IntegerField(blank=True, null=True)
	
	unit_time_part_2 = models.TextField(blank=True, null=True)
	
	unit_time_part_3 = models.TextField(blank=True, null=True)
	
	label_time_part_1 = models.TextField(blank=True, null=True)
	
	label_time_part_2 = models.TextField(blank=True, null=True)
	
	format_time_part_1 = models.TextField(blank=True, null=True)
	
	format_time_part_2 = models.TextField(blank=True, null=True)
	
	format_time_part_3 = models.TextField(blank=True, null=True)
	
	ener_e_2_part_1 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_2 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_3 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_5 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_7 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_8 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_9 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_11 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_12 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_13 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_14 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_15 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_17 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_18 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_19 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_20 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_21 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_23 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_24 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_25 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_26 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_27 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_28 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_30 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_31 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_32 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_33 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_34 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_36 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_37 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_38 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_39 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_40 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_42 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_43 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_44 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_45 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_46 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_48 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_49 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_50 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_51 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_52 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_54 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_55 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_1 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_2 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_3 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_4 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_6 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_7 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_8 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_9 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_10 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_12 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_13 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_14 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_15 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_16 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_18 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_19 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_20 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_21 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_22 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_24 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_25 = Float32Field(blank=True, null=True)
	
	epoch_1 = models.BigIntegerField(blank=True, null=True)
	
	epoch_2 = models.BigIntegerField(blank=True, null=True)
	
	time_pb5_1_part_3 = models.IntegerField(blank=True, null=True)
	
	time_pb5_3_part_3 = models.IntegerField(blank=True, null=True)
	
	fmode_4 = models.PositiveIntegerField(blank=True, null=True)
	
	a_theta_2 = Float32Field(blank=True, null=True)
	
	label_e_1_part_1 = models.TextField(blank=True, null=True)
	
	label_e_1_part_7 = models.TextField(blank=True, null=True)
	
	label_e_1_part_13 = models.TextField(blank=True, null=True)
	
	label_e_1_part_19 = models.TextField(blank=True, null=True)
	
	label_e_1_part_25 = models.TextField(blank=True, null=True)
	
	label_e_1_part_32 = models.TextField(blank=True, null=True)
	
	label_e_1_part_38 = models.TextField(blank=True, null=True)
	
	label_e_1_part_44 = models.TextField(blank=True, null=True)
	
	label_e_1_part_49 = models.TextField(blank=True, null=True)
	
	label_e_1_part_53 = models.TextField(blank=True, null=True)
	
	label_e_2_part_4 = models.TextField(blank=True, null=True)
	
	label_e_2_part_10 = models.TextField(blank=True, null=True)
	
	label_e_2_part_17 = models.TextField(blank=True, null=True)
	
	label_e_2_part_23 = models.TextField(blank=True, null=True)
	
	label_e_2_part_29 = models.TextField(blank=True, null=True)
	
	label_e_2_part_35 = models.TextField(blank=True, null=True)
	
	label_e_2_part_41 = models.TextField(blank=True, null=True)
	
	label_e_2_part_48 = models.TextField(blank=True, null=True)
	
	label_e_2_part_54 = models.TextField(blank=True, null=True)
	
	label_e_3_part_5 = models.TextField(blank=True, null=True)
	
	label_e_3_part_11 = models.TextField(blank=True, null=True)
	
	label_e_3_part_14 = models.TextField(blank=True, null=True)
	
	label_e_3_part_18 = models.TextField(blank=True, null=True)
	
	label_e_3_part_24 = models.TextField(blank=True, null=True)
	
	label_e_3_part_30 = models.TextField(blank=True, null=True)
	
	label_e_3_part_37 = models.TextField(blank=True, null=True)
	
	label_e_3_part_43 = models.TextField(blank=True, null=True)
	
	label_e_3_part_49 = models.TextField(blank=True, null=True)
	
	label_e_3_part_55 = models.TextField(blank=True, null=True)
	
	label_e_4_part_5 = models.TextField(blank=True, null=True)
	
	ener_e_4_part_27 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_28 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_29 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_30 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_31 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_33 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_34 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_35 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_36 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_37 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_39 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_40 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_41 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_42 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_43 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_44 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_46 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_47 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_48 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_49 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_50 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_52 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_53 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_54 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_55 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_56 = Float32Field(blank=True, null=True)
	
	gap_flag_2 = models.IntegerField(blank=True, null=True)
	
	gap_flag_4 = models.IntegerField(blank=True, null=True)
	
	label_e_4_part_12 = models.TextField(blank=True, null=True)
	
	label_e_4_part_18 = models.TextField(blank=True, null=True)
	
	label_e_4_part_24 = models.TextField(blank=True, null=True)
	
	label_e_4_part_30 = models.TextField(blank=True, null=True)
	
	label_e_4_part_33 = models.TextField(blank=True, null=True)
	
	label_e_4_part_37 = models.TextField(blank=True, null=True)
	
	label_e_4_part_43 = models.TextField(blank=True, null=True)
	
	label_e_4_part_49 = models.TextField(blank=True, null=True)
	
	label_e_4_part_56 = models.TextField(blank=True, null=True)
	
	ener_e_1_part_6 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_12 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_18 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_24 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_31 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_37 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_43 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_49 = Float32Field(blank=True, null=True)
	
	ener_e_1_part_52 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_1 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_8 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_14 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_20 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_26 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_32 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_39 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_45 = Float32Field(blank=True, null=True)
	
	ener_e_3_part_51 = Float32Field(blank=True, null=True)
	
	unit_time_part_1 = models.TextField(blank=True, null=True)
	
	label_time_part_3 = models.TextField(blank=True, null=True)
	
	ener_e_2_part_4 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_6 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_10 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_16 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_22 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_29 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_35 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_41 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_47 = Float32Field(blank=True, null=True)
	
	ener_e_2_part_53 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_5 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_11 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_17 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_23 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_26 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_32 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_38 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_45 = Float32Field(blank=True, null=True)
	
	ener_e_4_part_51 = Float32Field(blank=True, null=True)
	
	gap_flag_1 = models.IntegerField(blank=True, null=True)
	
	
	cdf_file = models.ForeignKey(CDFFileStored, on_delete=models.SET_NULL, related_name="INTERBALL_IT_H0_DOK_v01_data_data", db_index=False, blank=True, null=True)

	objects = GetManager()	
