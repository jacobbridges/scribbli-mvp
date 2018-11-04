from django.urls import path, re_path

from .views import LocationListView, LocationDetailView

urlpatterns = [
    path('worlds/', LocationListView.as_view(), name='location-list'),
    re_path('^worlds/(?P<slug>[a-z0-9_\-]+)/$', LocationDetailView.as_view(), name='location-detail'),
]