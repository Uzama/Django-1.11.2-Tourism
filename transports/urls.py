from django.conf.urls import url

from .views import TransportView, TransportProfile, TransportCreateView, transport_view

urlpatterns = [
    url(r'^$',transport_view),
    url(r'^create/$',TransportCreateView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$',TransportProfile.as_view()),
    ]