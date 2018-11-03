from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView
from django.urls.base import reverse

from scribbli.profiles.models import Profile


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'scribbli/profiles/detail.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        print('--------------------------------')
        print(f'{username}')
        try:
            return Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            raise Http404


class ProfileMyDetailRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user:
            return reverse('profile-detail', kwargs=dict(username=self.request.user.username))
        else:
            return reverse('/accounts/signup/')
