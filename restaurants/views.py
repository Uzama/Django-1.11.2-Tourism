from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q

from .models import Restaurant
from .forms import RestaurantCreate, RestaurantSearch
# Create your views here.
class RestaurantView(ListView):
	queryset = Restaurant.objects.all()

class RestaurantProfile(DetailView):
	queryset = Restaurant.objects.all()

class RestaurantCreateView(CreateView):
	form_class 	  = RestaurantCreate
	template_name = 'restaurants/create.html'
	success_url	  = '/restaurants'

def restaurant_view(request):
	template_name = 'restaurants/restaurant_list.html'
	print("hvvj")
	queryset	  = Restaurant.objects.all()
	form 		  = RestaurantSearch(request.POST or None)
	if form.is_valid():
		search 		= form.cleaned_data.get('search')
		filter_by	= form.cleaned_data.get('filter_by')
		sort_by		= form.cleaned_data.get('sort_by')
		order		= form.cleaned_data.get('order')

		if filter_by == 'name':
			if order == 'ascending':
				queryset = Restaurant.objects.filter(
						Q(name__iexact = search)|
						Q(name__icontains = search)
					).order_by(f'{sort_by}')
			else:
				queryset = Restaurant.objects.filter(
						Q(name__iexact = search)|
						Q(name__icontains = search)
					).order_by(f'-{sort_by}')
		elif filter_by == 'location':
			if order == 'ascending':
				queryset = Restaurant.objects.filter(
						Q(location__iexact = search)|
						Q(location__icontains = search)
					).order_by(f'{sort_by}')
			else:
				queryset = Restaurant.objects.filter(
						Q(location__iexact = search)|
						Q(location__icontains = search)
					).order_by(f'-{sort_by}')
		elif filter_by == 'district':
			if order == 'ascending':
				queryset = Restaurant.objects.filter(
						Q(district__iexact = search)|
						Q(district__icontains = search)
					).order_by(f'{sort_by}')
			else:
				queryset = Restaurant.objects.filter(
						Q(district__iexact = search)|
						Q(district__icontains = search)
					).order_by(f'-{sort_by}')
		elif filter_by == 'category':
			if order == 'ascending':
				queryset = Restaurant.objects.filter(
						Q(category__iexact = search)|
						Q(category__icontains = search)
					).order_by(f'{sort_by}')
			else:
				queryset = Restaurant.objects.filter(
						Q(category__iexact = search)|
						Q(category__icontains = search)
					).order_by(f'-{sort_by}')
	context = {
		'form':form,
		'object_list':queryset

	}
	print(context)

	return render(request, template_name, context)
