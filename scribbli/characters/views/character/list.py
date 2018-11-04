from django.contrib.auth.models import User
from django.views.generic import ListView

from ...models import Character


class CharacterListView(ListView):
    template_name = 'scribbli/characters/character/list.html'
    context_object_name = 'characters'

    def get_queryset(self):
        user_id = self.kwargs.get('user_id', None)

        if user_id is not None:
            return Character.objects.filter(user_id=user_id)
        return Character.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        user_id = self.kwargs.get('user_id', None)

        if user_id is not None:
            user = User.objects.get(id=user_id)
            context['page_title'] = f'{user.username} Characters'
        else:
            context['page_title'] = 'Character Directory'

        return context
