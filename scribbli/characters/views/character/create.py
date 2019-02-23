from django.http import Http404
from django.utils.text import slugify
from django.views.generic import CreateView

from scribbli.characters.models import Character


class CharacterCreateView(CreateView):
    template_name = 'scribbli/characters/character/create.html'
    model = Character
    fields = ['name']

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        try:
            form.instance.user = self.request.user
        except ValueError:
            raise Http404
        return form

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.name)
        return super().form_valid(form)
