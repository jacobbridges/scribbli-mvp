from django.db import models


class DateCreatedMixin(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    @property
    def created_timestamp(self):
        if self.date_created:
            return self.date_created.timestamp()
        else:
            return None


class DateModifiedMixin(models.Model):
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @property
    def modified_timestamp(self):
        if self.date_modified:
            return self.date_modified.timestamp()
        else:
            return None