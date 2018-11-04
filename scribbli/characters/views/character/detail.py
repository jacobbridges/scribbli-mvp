from django.views.generic import DetailView

from ...models import Character


class CharacterDetailView(DetailView):
    template_name = 'scribbli/characters/character/detail.html'
    context_object_name = 'character'
    model = Character
