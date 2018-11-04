from django.urls import path, re_path

from .views import CharacterListView, CharacterDetailView


urlpatterns = [
    path('directory/', CharacterListView.as_view(), name='character-list'),
    re_path('^(?P<pk>\d+)/(?P<slug>[a-z0-9_\-]+)/$', CharacterDetailView.as_view(), name='character-detail'),
]
