from django.db import models
from django.db.models.signals import pre_save

from .utils import unique_slug_generator
from .validators import (
	validate_name,
	validate_city,
	validate_district,
	validate_star,
	validate_price,
	validate_phone,

	)
# Create your models here.
class Hotel(models.Model):
	name			= models.CharField(max_length = 150, validators=[validate_name])
	city			= models.CharField(max_length = 100, validators=[validate_city])
	district		= models.CharField(max_length = 50, validators=[validate_district],null=True, blank=True)
	address			= models.CharField(max_length = 200,null=True, blank=True)
	star			= models.IntegerField(validators=[validate_star])
	price			= models.IntegerField(validators=[validate_price])
	phone_number	= models.IntegerField(validators=[validate_phone],null=True, blank=True)
	discription		= models.TextField(null=True, blank=True)
	slug 			= models.SlugField(null = True, blank = True)
	timestamp 		= models.DateTimeField(auto_now_add = True)
	updated			= models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.name

	@property
	def title(self):
		return self.name
	
def pre_save_reciver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_reciver, sender = Hotel)