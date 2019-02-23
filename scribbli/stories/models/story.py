from django.db import models
from django.urls.base import reverse
from django.contrib.auth.models import User

from scribbli.models.mixins import DateCreatedMixin, DateModifiedMixin
from scribbli.universe.models import Location


class Story(DateCreatedMixin, DateModifiedMixin, models.Model):
    """
    Stories are groups of posts.
    """
    name = models.CharField(max_length=80)
    slug = models.CharField(max_length=80)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='stories', null=True)
    locations = models.ManyToManyField(Location, related_name='stories')

    def get_absolute_url(self):
        return reverse('story-detail', kwargs=dict(slug=self.slug, pk=self.pk))

    def __str__(self): return self.name
