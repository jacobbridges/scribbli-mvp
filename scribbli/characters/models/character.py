from django.db import models
from django.contrib.auth.models import User
from django.urls.base import reverse

from scribbli.models.mixins import DateModifiedMixin, DateCreatedMixin


class Character(DateCreatedMixin, DateModifiedMixin, models.Model):
    """
    Characters are created by users and used to create stories in the multiverse.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='characters')
    name = models.CharField(max_length=80)
    slug = models.CharField(max_length=80)

    def get_absolute_url(self):
        return reverse('character-detail', kwargs=dict(slug=self.slug, pk=self.pk))

    def __str__(self): return self.name
