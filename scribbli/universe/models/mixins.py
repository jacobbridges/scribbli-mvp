from django.db import models

from scribbli.universe.models.universe import Universe


class BelongsToUniverseMixin(models.Model):
    universe = models.ForeignKey(Universe, on_delete=models.CASCADE, related_name='%(class)ss')

    class Meta:
        abstract = True