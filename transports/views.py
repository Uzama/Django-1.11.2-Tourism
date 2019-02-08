from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q

# Create your views here.
from .models import Transport
from .forms import TransportCreate, TransportSearch

class TransportView(ListView):
	queryset = Transport.objects.all()

class TransportProfile(DetailView):
	queryset = Transport.objects.all()

class TransportCreateView(CreateView):
	form_class = TransportCreate
	template_name = 'transports/create.html'
	success_url = '/transports'

def transport_view(request):
	template_name = 'transports/transport_list.html'
	form  = TransportSearch(request.POST or None)
	queryset = Transport.objects.all()
	if form.is_valid():
		search 		= form.cleaned_data.get('search')
		filter_by   = form.cleaned_data.get('filter_by')
		sort_by     = form.cleaned_data.get('sort_by')
		order		= form.cleaned_data.get('order')
		if filter_by == 'name':
			if order == 'ascending':
				queryset = Transport.objects.filter(
					Q(name__iexact = search)|
					Q(name__icontains = search)
					).order_by(f'{sort_by}')
			else:
				queryset = Transport.objects.filter(
					Q(name__iexact = search)|
					Q(name__icontains = search)
					).order_by(f'-{sort_by}')
		elif filter_by == 'capcity':
			if order == 'ascending':
				queryset = Transport.objects.filter(
					Q(capcity__iexact = search)|
					Q(capcity__icontains = search)
					).order_by(f'{sort_by}')
			else:
				queryset = Transport.objects.filter(
					Q(capcity__iexact = search)|
					Q(capcity__icontains = search)
					).order_by(f'-{sort_by}')
		elif filter_by == 'vehicle':
			if order == 'ascending':
				queryset = Transport.objects.filter(
					Q(vehicle__iexact = search)|
					Q(vehicle__icontains = search)
					).order_by(f'{sort_by}')
			else:
				queryset = Transport.objects.filter(
					Q(vehicle__iexact = search)|
					Q(vehicle__icontains = search)
					).order_by(f'-{sort_by}')
	context = {
		'form':form,
		'object_list':queryset

	}
	return render(request, template_name, context)

