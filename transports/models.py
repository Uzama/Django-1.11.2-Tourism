from django.db import models
from django.db.models.signals import pre_save

from .utils import unique_slug_generator
from .validators import (
		validate_name,
		validate_vehicle
	)
# Create your models here.
class Transport(models.Model):
	name			= models.CharField(max_length=100, validators=[validate_name])
	vehicle			= models.CharField(max_length=50, validators=[validate_vehicle])
	capcity			= models.IntegerField(null=True, blank=True)
	phone			= models.IntegerField(null=True, blank=True)
	price			= models.IntegerField(null=True, blank=True)
	timestamp		= models.DateTimeField(auto_now_add=True)
	updated			= models.DateTimeField(auto_now=True)
	slug			= models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def title(self):
		return self.name
	
def pre_save_reciver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_reciver, sender = Transport)