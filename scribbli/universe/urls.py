from django.urls import path, re_path

from .views import (
    LocationListView,
    LocationDetailView,
    LocationCreateView,
    LocationUpdateView,
    LocationStoryListView,
)

urlpatterns = [
    path('worlds/', LocationListView.as_view(), name='location-list'),
    path('worlds/new/', LocationCreateView.as_view(), name='location-create'),
    path('worlds/<int:pk>/<slug:slug>/', LocationDetailView.as_view(), name='location-detail'),
    path('worlds/<int:pk>/<slug:slug>/edit/', LocationUpdateView.as_view(), name='location-update'),
    path('worlds/<int:pk>/<slug:slug>/stories/', LocationStoryListView.as_view(), name='location-story-list'),
]