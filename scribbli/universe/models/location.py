from django.db import models
from django.urls.base import reverse
from mptt.models import MPTTModel, TreeForeignKey

from dsms import Serializable
from scribbli.models.mixins import DateCreatedMixin, DateModifiedMixin


class Location(MPTTModel, DateCreatedMixin, DateModifiedMixin, Serializable):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    @property
    def unique_name(self):
        return f'{self.name}#{self.id:04}'

    def serialize(self):
        data = super().serialize()
        data.update(dict(
            name=self.name,
            slug=self.slug,
            parent=(None if self.parent is None else self.parent.serialize()),
        ))
        return data

    def get_absolute_url(self):
        return reverse('location-detail', kwargs=dict(slug=self.slug))

    def __repr__(self): return self.unique_name

    def __unicode__(self): return self.unique_name

    def __str__(self): return self.unique_name
