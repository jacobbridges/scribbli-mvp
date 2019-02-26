from django.views.generic import ListView

from ...models import Character


class CharacterListView(ListView):
    template_name = 'scribbli/characters/character/list.html'
    context_object_name = 'characters'
    model = Character
    paginate_by = 10
