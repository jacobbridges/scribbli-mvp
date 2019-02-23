from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.forms import ModelForm
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from mptt.exceptions import InvalidMove

from ..models import Location


class LocationListView(ListView):
    template_name = 'scribbli/universe/location/list.html'
    context_object_name = 'locations'
    queryset = Location.objects.filter(parent_id__isnull=True)
    paginate_by = 10


class LocationDetailView(DetailView):
    template_name = 'scribbli/universe/location/detail.html'
    context_object_name = 'location'
    model = Location


class LocationCreateView(LoginRequiredMixin, CreateView):
    template_name = 'scribbli/universe/location/create.html'
    model = Location
    fields = ['name', 'parent']

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.name)
        return super().form_valid(form)


class LocationUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'scribbli/universe/location/update.html'
    model = Location
    fields = ['name', 'parent']

    def form_valid(self, form: ModelForm):
        form.instance.slug = slugify(form.instance.name)
        try:
            return super(LocationUpdateView, self).form_valid(form)
        except InvalidMove:
            form.add_error(
                'parent',
                ValidationError('World cannot be its own parent!', code='invalid')
            )
            return self.form_invalid(form)
