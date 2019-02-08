from django.utils.text import slugify

import random

not_slug = ['create']
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def random_string(size):
	string = ''
	for i in range(size):
		string += str(alpha[random.randint(0,26)])
	return string

def unique_slug_generator(instance, new_slug=None):
	if new_slug is not None:
		slug = new_slug
	else:
		slug = slugify(instance.title)
	if slug in not_slug:
		slug = slug
		rand_string = random_string(4)
		new_slug = f'{slug}-{rand_string}'
		return unique_slug_generator(instance, new_slug)
	Klass = instance.__class__
	slug_exist = Klass.objects.filter(slug = slug)
	if slug_exist:
		slug = slug
		rand_string = random_string(4)
		new_slug = f'{slug}-{rand_string}'
		return unique_slug_generator(instance, new_slug)
	return slug
