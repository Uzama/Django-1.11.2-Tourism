from django import forms

from .models import Place

class PlaceCreate(forms.ModelForm):
	class Meta:
		model  = Place
		fields = [
			'name', 		
			'location',	
			'district',    
			'popular_for', 
			'price',		
			'bio',
			] 	

class SearchPlace(forms.Form):
	search      = forms.CharField()
	filter_by 	= forms.ChoiceField(required = True, label='', choices=(
			('name',("name")),
			('location',("location")),
			('district',("district")),
			('popular_for',("popular_for")),
		))
	sort_by		= forms.ChoiceField(label='', choices=(
			('updated',("updated")),
			('timestamp',("timestamp")),
			('name',("name")),
			('location',("location")),
		))
	order 		= forms.ChoiceField(label='',choices=(
			("ascending", ("ascending")),
            ("descending", ("descending"))
        ))
