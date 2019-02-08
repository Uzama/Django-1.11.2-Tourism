from django.core.exceptions import ValidationError

def validate_name(value):
	list1 = value.split(' ')
	for i in list1:
		if not i.isalpha():
			raise ValidationError(f'{value} is wrong')

def validate_vehicle(value):
	if value.capitalize() not in ['Car','Bus','Van','Lorry']:
		raise ValidationError(f'{value} is wrong')

