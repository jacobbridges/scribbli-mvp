from django.urls import path

from .views import StoryListView, StoryDetailView


urlpatterns = [
    path('/', StoryListView.as_view(), name='story-list'),
    path('<slug:slug>/<int:pk>/', StoryDetailView.as_view(), name='story-detail'),
]
