from django.apps import AppConfig


class ScribbliConfig(AppConfig):
    name = 'scribbli'
    label = 'scribbli'

    def ready(self):
        from scribbli.signals.slug import handle_slug