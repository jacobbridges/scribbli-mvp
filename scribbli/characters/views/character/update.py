from django.utils.text import slugify
from django.views.generic import UpdateView

from scribbli.characters.models import Character


class CharacterUpdateView(UpdateView):
    template_name = 'scribbli/characters/character/update.html'
    model = Character
    fields = ['name']

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.name)
        return super().form_valid(form)
