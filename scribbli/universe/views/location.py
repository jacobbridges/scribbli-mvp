from django.views.generic import ListView, DetailView

from ..models import Location


class LocationListView(ListView):
    template_name = 'scribbli/universe/location/list.html'
    context_object_name = 'locations'
    queryset = Location.objects.filter(parent_id__isnull=True)


class LocationDetailView(DetailView):
    template_name = 'scribbli/universe/location/detail.html'
    context_object_name = 'location'
    model = Location
