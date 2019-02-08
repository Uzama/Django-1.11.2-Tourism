from django.db import models
from django.db.models.signals import pre_save

from .utils import unique_slug_generator
from .validators import (
	validate_name,
	validate_district,

	)
# Create your models here.
class Place(models.Model):
	name 		= models.CharField(max_length=200, validators=[validate_name])
	location	= models.CharField(max_length=150, null=True, blank=True)
	district    = models.CharField(max_length=50, validators=[validate_district])
	popular_for = models.CharField(max_length=200, validators=[validate_name])
	price		= models.IntegerField()
	bio 		= models.TextField(null=True, blank=True)
	slug		= models.SlugField(null=True, blank=True)
	timestamp   = models.DateTimeField(auto_now_add=True)
	updated		= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	@property
	def title(self):
		return self.name
	
def pre_save_reciver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_reciver, sender = Place)