from django.views.generic import DetailView, ListView

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
