from django.db import models
from django.urls.base import reverse
from mptt.models import MPTTModel, TreeForeignKey

from scribbli.models.mixins import DateCreatedMixin, DateModifiedMixin


class Location(MPTTModel, DateCreatedMixin, DateModifiedMixin):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    @property
    def unique_hash(self):
        return f'{self.id:04}'

    @property
    def unique_name(self):
        return f'{self.name}#{self.unique_hash}'

    def get_absolute_url(self):
        return reverse('location-detail', kwargs=dict(pk=self.pk, slug=self.slug))

    def __str__(self): return self.unique_name
