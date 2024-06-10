import os

from django.core.management import BaseCommand
from dotenv import load_dotenv

load_dotenv()


class Command(BaseCommand):
    help = 'Create a superuser if it does not exist'

    def handle(self, *args, **options) -> None:
        from django.contrib.auth.models import User

        username = os.getenv('DJANGO_SUPERUSER_USERNAME')
        email = os.getenv('DJANGO_SUPERUSER_EMAIL')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

        if not User.objects.filter(username=username).exists():
            print("[INFO] Creating superuser...")
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
            )
            print("[INFO] Superuser created.")

        else:
            print("[INFO] Superuser already exists.")
