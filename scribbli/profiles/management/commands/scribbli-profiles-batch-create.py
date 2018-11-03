import logging

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from ...models import Profile


class Command(BaseCommand):
    help = 'Create profiles for any user without a profile.'
    log = logging.getLogger(__name__)

    def handle(self, *args, **options):
        self.log.setLevel(logging.DEBUG)
        users_without_profiles = User.objects.filter(profile__isnull=True)

        if users_without_profiles.exists():
            self.log.info(f'Adding profiles for {users_without_profiles.count()} users...')
            for user in users_without_profiles:
                Profile.objects.create(user=user)

        else:
            self.log.info('No users found missing a profile.')

        self.log.info('Done')
