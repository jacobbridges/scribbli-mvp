from django.urls.base import reverse
from django.db import models

from dsms import Serializable


class Universe(models.Model, Serializable):
    """
    A universe is home to potentially infinite locations.
    """

    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)

    def serialize(self):
        data = super().serialize()
        data.update(dict(
            name=self.name,
            slug=self.slug,
        ))
        return data

    def get_absolute_url(self):
        return ''


class BelongsToUniverse(models.Model, Serializable):
    universe = models.ForeignKey(Universe, on_delete=models.CASCADE, related_name='%(class)ss')

    class Meta:
        abstract = True

    def serialize(self):
        data = super().serialize()
        data.update({
            'universe': self.universe.name,
            'universe_id': self.universe.id,
            'universe_url': self.universe.get_absolute_url(),
        })
        return data
