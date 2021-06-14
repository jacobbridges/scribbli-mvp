from django.db import models
from django.urls.base import reverse
from mptt.models import MPTTModel, TreeForeignKey

from scribbli.models.mixins import DateCreatedMixin, DateModifiedMixin
from scribbli.universe.models.mixins import BelongsToUniverseMixin


class Location(MPTTModel, DateCreatedMixin, DateModifiedMixin, BelongsToUniverseMixin):
    """Location is any area within a universe.
    
    A galaxy is a location.
    A world is a location.
    A city is a location.
    A alley is a location.

    Anywhere a writer finds useful to point out and have the story take 
    you can be a location.
    """

    SLUG_MAP = {
        "name": "slug"
    }

    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    @property
    def unique_name(self):
        return f'{self.name}#{self.id:04}'

    def get_absolute_url(self):
        return reverse('location-detail', kwargs=dict(pk=self.pk, slug=self.slug))

    def __str__(self): return self.unique_name
