from django.db import models
from django.urls.base import reverse

from scribbli.models.mixins import DateCreatedMixin, DateModifiedMixin
from dsms import Serializable


class Story(DateCreatedMixin, DateModifiedMixin, models.Model, Serializable):
    """
    Stories are groups of posts.
    """
    name = models.CharField(max_length=80)
    slug = models.CharField(max_length=80)

    def get_absolute_url(self):
        return ''

    def serialize(self):
        data = super().serialize()
        data.update(dict(
            name=self.name,
            slug=self.slug,
            url=self.get_absolute_url(),
        ))
