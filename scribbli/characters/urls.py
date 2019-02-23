from django.urls import path

from .views import (
    CharacterListView,
    CharacterDetailView,
    CharacterCreateView,
    CharacterUpdateView,
)


urlpatterns = [
    path('', CharacterListView.as_view(), name='character-list'),
    path('new/', CharacterCreateView.as_view(), name='character-create'),
    path('<int:pk>/<slug:slug>/', CharacterDetailView.as_view(), name='character-detail'),
    path('<int:pk>/<slug:slug>/edit/', CharacterUpdateView.as_view(), name='character-update'),
]
