from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from django.views.generic import DetailView, ListView, UpdateView, CreateView

from ..models import Story


class StoryDetailView(DetailView):
    context_object_name = 'story'
    model = Story
    template_name = 'scribbli/stories/story/detail.html'


class StoryListView(ListView):
    context_object_name = 'stories'
    model = Story
    template_name = 'scribbli/stories/story/list.html'
    paginate_by = 10


class StoryCreateView(LoginRequiredMixin, CreateView):
    template_name = 'scribbli/stories/story/create.html'
    model = Story
    fields = ['name', 'description', 'locations']

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.instance.user = self.request.user
        return form

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.name)
        return super().form_valid(form)


class StoryUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'scribbli/stories/story/update.html'
    model = Story
    fields = ['name', 'description', 'locations']

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.name)
        return super().form_valid(form)
