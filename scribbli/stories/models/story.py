from django.db import models
from django.urls.base import reverse

from scribbli.models.mixins import DateCreatedMixin, DateModifiedMixin


class Story(DateCreatedMixin, DateModifiedMixin, models.Model):
    """
    Stories are groups of posts.
    """
    name = models.CharField(max_length=80)
    slug = models.CharField(max_length=80)

    def get_absolute_url(self):
        return ''
