from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from scribbli.profiles.constants import RoleChoices


class Profile(models.Model):
    """
    Profiles store additional information about site users, relating back to Django's auth_user.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(default=RoleChoices.Guest, choices=RoleChoices.as_choices())
    about = models.CharField(max_length=500, blank=True)

    @staticmethod
    def create_profile_on_user_create(sender, instance, created, **kwargs):
        """
        Signal handler which creates a profile for newly created users.
        """
        if not created: return
        Profile.objects.create(user=instance)


post_save.connect(Profile.create_profile_on_user_create, sender=User, dispatch_uid='create_profile_on_user_create')
