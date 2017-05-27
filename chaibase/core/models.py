from uuid import uuid4


from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser
from django.db.models import Model, UUIDField, CharField, DateTimeField, \
    ForeignKey, ManyToManyField, FloatField, BooleanField, \
    PositiveSmallIntegerField

from phonenumber_field.modelfields import PhoneNumberField
from django_google_maps.fields import AddressField, GeoLocationField

from chaibase.core.enums import LeafGrade


class User(AbstractUser):
    '''
    A custom user so that we can add permissions easily
    '''
    uuid = UUIDField(default=uuid4, primary_key=True, editable=False)
    socket_id = UUIDField(
        default=uuid4, editable=False, db_index=True, unique=True)
    phone_number = PhoneNumberField(blank=True)
    expiry = DateTimeField(default=now)

    class Meta(AbstractUser.Meta):
        abstract = False
        unique_together = ('email',)


class BaseModel(Model):
    '''
    This shoud be inherited by all the classes whose objects are created due
    to user interaction.
    '''
    uuid = UUIDField(default=uuid4, primary_key=True, editable=False)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.uuid)

    def __repr__(self):

        return f'<{self.__class__.__name__}: {self.__str__()}>'


class Location(BaseModel):
    '''
    Factory Model
    '''
    address = AddressField(max_length=200)
    geolocation = GeoLocationField(max_length=100)

    def __str__(self):
        return f'{self.address}:{self.geolocation}'


class Factory(BaseModel):
    '''
    Factory Model
    '''
    name = CharField(max_length=100)
    owner = ForeignKey(User, related_name='owned_factories')
    location = ForeignKey(Location, related_name='factories')
    phone_number = PhoneNumberField(blank=True)

    def __str__(self):
        return f'{self.name}:{self.owner}'


class Vehicle(BaseModel):
    number = CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.number}'


class Person(BaseModel):
    '''
    Project Model
    '''
    factories = ManyToManyField(Factory, related_name='people')
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30, null=True, blank=True)
    nick_name = CharField(max_length=30, null=True, blank=True)
    initials = CharField(max_length=10, null=True, blank=True)
    home_number = PhoneNumberField(blank=True)
    mobile_number = PhoneNumberField(blank=True)
    office_number = PhoneNumberField(blank=True)
    location = ForeignKey(Location, related_name='people')

    def __str__(self):
        return f'{self.first_name}:{self.last_name}:{self.nick_name}'


class Weighment(BaseModel):
    factory = ForeignKey(Factory, related_name="weighments")
    person = ForeignKey(Person, related_name="weighments")
    vehicle = ForeignKey(Vehicle, related_name="weighments")
    date = DateTimeField(default=now)

    def __str__(self):
        return f'f({self.factory}):p({self.person}):v({self.vehicle})'\
            ':d({self.date})'


class Entry(BaseModel):
    weight = FloatField(default=0.0)
    is_confirmed = BooleanField(default=False)
    weighment = ForeignKey(Weighment, related_name="entries")
    grade = PositiveSmallIntegerField(
        default=LeafGrade.UNKNOWN, choices=LeafGrade.CHOICES)

    def __str__(self):
        return f'w({self.weighment}):{self.weight}:{self.is_confirmed}'\
            ':{self.get_grade_display()}'
