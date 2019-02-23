from django.db import models
from django.urls.base import reverse

from .story import Story
from scribbli.models.mixins import DateCreatedMixin, DateModifiedMixin


class Post(DateCreatedMixin, DateModifiedMixin, models.Model):
    """
    Posts are pieces of a story.
    """
    content = models.CharField(max_length=2500)
