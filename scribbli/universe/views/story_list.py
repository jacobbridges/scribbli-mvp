from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from scribbli.universe.models import Location


class LocationStoryListView(ListView):
    template_name = 'scribbli/universe/location/story-list.html'
    context_object_name = 'stories'

    def get(self, request, *args, **kwargs):
        location_pk = kwargs.get('pk')
        self.location = get_object_or_404(Location, pk=location_pk)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return self.location.stories.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['location'] = self.location
        return context
