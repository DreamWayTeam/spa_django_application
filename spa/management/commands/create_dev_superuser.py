from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Create test superuser, use for DEV environment only!'

    def handle(self, **_):  # pylint: disable=arguments-differ
        User = get_user_model()  # noqa pylint: disable=invalid-name
        if not User.objects.filter(username=settings.DEV_SUPERUSER_USERNAME).exists():
            User.objects.create_superuser(
                username=settings.DEV_SUPERUSER_USERNAME, password=settings.DEV_SUPERUSER_PASSWORD
            )
        self.stdout.write(
            "!!! Pay attention: DEV Superuser '{email}/{pw}' is active !!!".format(
                email=settings.DEV_SUPERUSER_USERNAME, pw=settings.DEV_SUPERUSER_PASSWORD))
