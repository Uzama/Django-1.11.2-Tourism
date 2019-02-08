from django import forms

from .models import Restaurant

class RestaurantCreate(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields = [
			'name',		
			'location',
			'district',	
			'category',	
			'phone',		
			'bio', 		
		]

class RestaurantSearch(forms.Form):
	search 			= forms.CharField(label='')
	filter_by		= forms.ChoiceField(label='', choices=(
				('name',('name')),
				('location',('location')),
				('district',('district')),
				('category',('category')),
		))
	sort_by			= forms.ChoiceField(label='', choices=(
				('updated',('updated')),
				('timestamp',('timestamp')),
				('name',('name')),
				('location',('location')),

		))
	order			= forms.ChoiceField(label='', choices=(
				('ascending',('ascending')),
				('descending',('descending')),
		))