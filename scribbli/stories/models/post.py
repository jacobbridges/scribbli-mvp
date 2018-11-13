from django.db import models
from django.urls.base import reverse

from .story import Story
from scribbli.models.mixins import DateCreatedMixin, DateModifiedMixin
from dsms import Serializable


class Post(DateCreatedMixin, DateModifiedMixin, models.Model, Serializable):
    """
    Posts are pieces of a story.
    """
    content = models.CharField(max_length=2500)
