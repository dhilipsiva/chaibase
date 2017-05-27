import maya

from django.conf import settings
from django.core.management.base import BaseCommand

from chaibase.importers.teapack import Suppliermst, Vehiclemst, Leafsupplyhdr
from chaibase.core.dbapi import get_person, create_person, get_factory, \
    get_vehicle, create_vehicle, get_weighment, create_weighment

factory = get_factory(name=settings.DEMO_FACTORY)
print(factory)


class Command(BaseCommand):
    help = "Import things from teapack"

    # def add_arguments(self, parser):
    #     parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):
        for supplier in Suppliermst.select():
            person = get_person(full_name=supplier.msuppliername)
            if person is None:
                person = create_person(full_name=supplier.msuppliername)
            print(person)
        for _vehicle in Vehiclemst.select():
            vehicle = get_vehicle(number=_vehicle.mvehiclename)
            if vehicle is None:
                vehicle = create_vehicle(number=_vehicle.mvehiclename)
            print(vehicle)
        for supply_header in Leafsupplyhdr.select():
            _date = maya.parse(str(supply_header.msupplydate)).datetime()
            person = get_person(full_name=supply_header.msuppliername)
            if person is None:
                person = create_person(full_name=supply_header.msuppliername)
            vehicle = get_vehicle(number=supply_header.mvehiclename)
            kwargs = dict(
                date=_date, person=person, factory=factory,
                vehicle=vehicle)
            weighment = get_weighment(**kwargs)
            if weighment is None:
                weighment = create_weighment(**kwargs)
            print(weighment)
