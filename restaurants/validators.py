from django.core.exceptions import ValidationError

def validate_name(value):
	list1 = value.split(' ')
	for i in list1:
		if not i.isalpha():
			raise ValidationError(f"{value} is wrong")

def validate_district(value):
	if value.capitalize() not in ['Kandy', 'Colombo', 'Jaffna']:
		raise ValidationError(f'{value} is wrong')

def validate_category(value):
	if value.capitalize() not in ['Srilankan', 'Chinese', 'Indian', 'American', 'Asian']:
		raise ValidationError(f'{value} is wrong')