from django.core.exceptions import ValidationError

alpha_c = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
alpha_s = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
districts = ['Kandy','Colombo','Kalutara','Gampaha','Galle','Jaffna']
def validate_name(value):
	name = ''.join(value.split())
	for i in list(name):
		if (i not in alpha_s) and (i not in alpha_c):
			raise ValidationError(f"{value} is incorrect name")

def validate_city(value):
	city = ''.join(value.split())
	for i in list(city):
		if (i not in alpha_s) and (i not in alpha_c):
			raise ValidationError(f"{value} is incorrect city")

def validate_district(value):
	district = value
	if district.capitalize() not in districts:
		raise ValidationError(f'{district} is wrong')

def validate_star(value):
	if value not in [1,2,3,4,5]:
		raise ValidationError("Star is between 1-5")

def validate_price(value):
	if value < 0:
		raise ValidationError("Price should be possitive")

def validate_phone(value):
	print(value)
	if (value < 0) or (len(list(str(value))) != 9):
		raise ValidationError("wrong phone number")