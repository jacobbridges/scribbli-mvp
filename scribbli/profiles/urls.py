from django.urls import re_path

from .views import ProfileDetailView, ProfileMyDetailRedirectView


urlpatterns = [
    re_path(r'^(?P<username>[A-Za-z0-9_\-]+)/$', ProfileDetailView.as_view(), name='profile-detail'),
    re_path(r'^\$/$', ProfileMyDetailRedirectView.as_view(), name='profile-detail--mine'),
]
