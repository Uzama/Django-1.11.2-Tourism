from django.conf.urls import url

from .views import RestaurantView, RestaurantProfile, RestaurantCreateView, restaurant_view

urlpatterns = [
    url(r'^$',restaurant_view),
    url(r'^create/$',RestaurantCreateView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$',RestaurantProfile.as_view()),
    ]