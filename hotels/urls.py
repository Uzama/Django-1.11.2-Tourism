from django.conf.urls import url
from .views import HotelView, HotelProfile, HotelCreateView, hotel_view

urlpatterns = [
	url(r'^$',hotel_view),
	url(r'^create/$',HotelCreateView.as_view()),
	url(r'^(?P<slug>[\w-]+)/$',HotelProfile.as_view()),
]