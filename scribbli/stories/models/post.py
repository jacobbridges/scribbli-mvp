from django.db import models
from django.urls.base import reverse

from .story import Story
from scribbli.characters.models import Character
from scribbli.models.mixins import DateCreatedMixin, DateModifiedMixin


class Post(DateCreatedMixin, DateModifiedMixin, models.Model):
    """
    Posts are pieces of a story.
    """
    content = models.CharField(max_length=4500)
    story = models.ForeignKey(Story, on_delete=models.SET_NULL, related_name='posts', null=True)
    character = models.ForeignKey(Character, on_delete=models.SET_NULL, related_name='posts', null=True)
