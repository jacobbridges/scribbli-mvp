from django.urls.base import reverse
from django.db import models


class Universe(models.Model):
    """A universe is home to potentially infinite locations."""

    SLUG_MAP = {
        "name": "slug"
    }

    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)

    @classmethod
    def alpha(cls):
        return Universe.objects.get_or_create(
            name='Alpha',
            slug='alpha'
        )[0]

    @property
    def unique_name(self):
        return f'{self.name}#{self.id:04}'

    def get_absolute_url(self):
        return ''

    def __str__(self): return self.unique_name
