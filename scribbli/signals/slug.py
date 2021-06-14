from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from scribbli.universe.models import (
    Location,
    Universe,
)


@receiver(pre_save, sender=Location, dispatch_uid="location_pre_save_slugify")
@receiver(pre_save, sender=Universe, dispatch_uid="universe_pre_save_slugify")
def handle_slug(sender, **kwargs):
    """Calculate the slug on a model instance based on the value of a field."""
    instance = kwargs.get("instance")
    for value_field, slug_field in instance.SLUG_MAP.items():
        setattr(instance, slug_field, slugify(getattr(instance, value_field)))
