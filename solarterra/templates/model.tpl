from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid
from solarterra.abstract_models import GetManager
from load_cdf.models import CDFFileStored, Float32Field

class {{ dm_instance.model_name }}(models.Model):

	{% for field in rendered_fields %}
	{{ field.name }} = {{ field.definition }}
	{% endfor %}
	
	cdf_file = models.ForeignKey(CDFFileStored, on_delete=models.SET_NULL, related_name="{{ dm_instance.model_name}}_data", db_index=False, blank=True, null=True)

	objects = GetManager()	
