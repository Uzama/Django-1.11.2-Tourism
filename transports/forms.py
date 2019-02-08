from django import forms

from .models import Transport

class TransportCreate(forms.ModelForm):
	class Meta:
		model = Transport
		fields = [
			'name',			
			'vehicle',			
			'capcity',		
			'phone',		
			'price',			
		]

class TransportSearch(forms.Form):
	search 		= forms.CharField(label='')
	filter_by	= forms.ChoiceField(label='', choices=(
			('name',('name')),
			('capcity',('capcity')),
			('vehicle',('vehicle')),
		))

	sort_by 	= forms.ChoiceField(label='', choices=(
			('updated',('updated')),
			('timestamp',('timestamp')),
			('name',('name')),
			('capcity',('capcity')),
		))

	order		= forms.ChoiceField(label='', choices=(
			('ascending',('ascending')),
			('descending',('descending')),
		))