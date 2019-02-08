from django import forms 

from .models import Hotel

class HotelCreate(forms.ModelForm):
	class Meta:
		model = Hotel
		fields = [
			'name',			
			'city',			
			'district',		
			'address',			
			'star',			
			'price',			
			'phone_number',	
			'discription'		
		]

class HotelSearch(forms.Form):
	filter_by 			= 	forms.ChoiceField(label='',choices=(("all", ("all")),
                                        ("location", ("location")),
                                        ("name", ("name")),
                                        ("star", ("star"))))
	search 				= 	forms.CharField(label='',required=True)
	sort_by 			= 	forms.ChoiceField(label='',choices=(
                                        ("timestamp", ("created")),
                                        ("updated", ("updated")),
                                        ("name", ("name")),
                                        ("district", ("district"))))
	order 			= 	forms.ChoiceField(label='',choices=(("ascending", ("ascending")),
                                        ("descending", ("descending"))))

	# def clean_filter_by(self):

	# 	value = self.cleaned_data.get('filter_by')
	# 	print(value)
	# 	if int(value) not in [1,2,3]:
	# 		print('w')
	# 		raise forms.ValidationError("wrong Input")