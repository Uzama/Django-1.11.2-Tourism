from django.conf.urls import url

from .views import PlaceView, PlaceProfile, PlaceCreateView, place_view

urlpatterns = [
    url(r'^$', place_view),
    url(r'^create/$', PlaceCreateView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', PlaceProfile.as_view()),

    ]