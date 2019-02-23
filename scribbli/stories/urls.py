from django.urls import path

from .views import (
    StoryListView,
    StoryDetailView,
    StoryCreateView,
    StoryUpdateView,
)


urlpatterns = [
    path('', StoryListView.as_view(), name='story-list'),
    path('new/', StoryCreateView.as_view(), name='story-create'),
    path('<slug:slug>/<int:pk>/', StoryDetailView.as_view(), name='story-detail'),
    path('<slug:slug>/<int:pk>/edit/', StoryUpdateView.as_view(), name='story-update'),
]
