from django.urls.base import reverse
from django.db import models


class Universe(models.Model):
    """
    A universe is home to potentially infinite locations.
    """

    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)

    def get_absolute_url(self):
        return ''


class BelongsToUniverse(models.Model):
    universe = models.ForeignKey(Universe, on_delete=models.CASCADE, related_name='%(class)ss')

    class Meta:
        abstract = True
