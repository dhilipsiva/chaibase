from django.conf import settings
from django.core.management.base import BaseCommand

from chaibase.core.dbapi import create_user, create_factory, get_factory, \
    get_user_by_username


class Command(BaseCommand):
    help = "Seed Database"

    # def add_arguments(self, parser):
    #     parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):
        user = get_user_by_username("dhilipsiva")
        if user is None:
            user = create_user(
                username="dhilipsiva", password="test1234", is_staff=True,
                is_superuser=True)
        print(user)
        factory = get_factory(owner=user, name=settings.DEMO_FACTORY)
        if factory is None:
            factory = create_factory(owner=user, name=settings.DEMO_FACTORY)
        print(factory)
