from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q


from . forms import PlaceCreate, SearchPlace
from .models import Place
# Create your views here.
class PlaceView(ListView):
	queryset = Place.objects.all()

class PlaceProfile(DetailView):
	queryset = Place.objects.all()

class PlaceCreateView(CreateView):
	form_class  = PlaceCreate
	template_name    = 'places/create.html'
	success_url = '/places'

def place_view(request):
	template_name = 'places/place_list.html'
	form = SearchPlace(request.POST or None)
	queryset = Place.objects.all()
	if form.is_valid():
		search      = form.cleaned_data.get('search')
		filter_by   = form.cleaned_data.get('filter_by')
		sort_by		= form.cleaned_data.get('sort_by')
		order		= form.cleaned_data.get('order')
		print(search)
		if filter_by == 'name':
			if order == 'ascending':
				queryset = Place.objects.filter(
						Q(name__iexact = search) |
						Q(name__icontains = search)
					).order_by(f'{sort_by}')
			else:
				queryset = Place.objects.filter(
						Q(name__iexact = search) |
						Q(name__icontains = search)
					).order_by(f'-{sort_by}')
		elif filter_by == 'location':
			if order == 'ascending':
				queryset = Place.objects.filter(
						Q(location__iexact = search) |
						Q(location__icontains = search)
					).order_by(f'{sort_by}')
			else:
				queryset = Place.objects.filter(
						Q(location__iexact = search) |
						Q(location__icontains = search)
					).order_by(f'-{sort_by}')
		elif filter_by == 'district':
			if order == 'ascending':
				queryset = Place.objects.filter(
						Q(district__iexact = search) |
						Q(district__icontains = search)
					).order_by(f'{sort_by}')
			else:
				queryset = Place.objects.filter(
						Q(district__iexact = search) |
						Q(district__icontains = search)
					).order_by(f'-{sort_by}')
		elif filter_by == 'popular_for':
			if order == 'ascending':
				queryset = Place.objects.filter(
						Q(popular_for__iexact = search) |
						Q(popular_for__icontains = search)
					).order_by(f'{sort_by}')
			else:
				queryset = Place.objects.filter(
						Q(popular_for__iexact = search) |
						Q(popular_for__icontains = search)
					).order_by(f'-{sort_by}')


	context = {
		'form':form,
		'object_list':queryset,
		}
	return render(request, template_name, context)
