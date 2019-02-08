from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.db.models import Q

from .models import Hotel
from .forms import HotelCreate, HotelSearch
# Create your views here.
# def hotel(request):
# 	template_name = 'hotel.html'
# 	list1 = ["Galladary", "Chinnamangrand", "Sangarilla"]
# 	context = {'hotels':list1}
# 	return render(request, template_name, context)

class HomeView(TemplateView):
	template_name = 'home.html'

class AboutView(TemplateView):
	template_name = 'about.html'

class HotelView(ListView):
	queryset = Hotel.objects.all()
	# def get_queryset(self, *args, **kwargs):
	# 	queryset = super(HotelView, self).get_queryset(*args, **kwargs)
	# 	queryset = Hotel.objects.all()
	# 	return queryset
class HotelProfile(DetailView):
	queryset = Hotel.objects.all()

class HotelCreateView(CreateView):
	form_class = HotelCreate
	template_name = 'hotels/hotel_form.html'
	success_url = '/hotels'

def hotel_view(request):
	template_name = 'hotels/hotel_list.html'
	# place_holder  = ''
	object_list = Hotel.objects.all()
	form = HotelSearch(request.POST or None)
	if form.is_valid():
		filter_by = form.cleaned_data.get('filter_by')
		search    = form.cleaned_data.get('search')
		sort_by	  = form.cleaned_data.get('sort_by')
		order     = form.cleaned_data.get('order')
		if filter_by == 'name':
			if order == 'ascending':
				object_list = Hotel.objects.filter(

					Q(name__iexact =search) |
					Q(name__icontains =search)

					).order_by(f'{sort_by}')
			else:
				object_list = Hotel.objects.filter(

					Q(name__iexact =search) |
					Q(name__icontains =search)

					).order_by(f'-{sort_by}')
		elif filter_by == 'location':
			if order == 'ascending':
				object_list = Hotel.objects.filter(

					Q(district__iexact =search) |
					Q(district__icontains =search)

					).order_by(f'{sort_by}')
			else:
				object_list = Hotel.objects.filter(

					Q(district__iexact =search) |
					Q(district__icontains =search)

					).order_by(f'-{sort_by}')
		elif filter_by == 'star':
			if order == 'ascending':
				object_list = Hotel.objects.filter(

					Q(star__iexact =search) |
					Q(star__icontains =search)

					).order_by(f'{sort_by}')
			else:
				object_list = Hotel.objects.filter(

					Q(star__iexact =search) |
					Q(star__icontains =search)

					).order_by(f'-{sort_by}')
		elif filter_by == 'all':
			if order == 'ascending':
				object_list = Hotel.objects.all().order_by(f'{sort_by}')
			else:
				object_list = Hotel.objects.all().order_by(f'-{sort_by}')


	context = {
	'object_list':object_list,
	'form':form,
	}
	return render(request, template_name, context)


