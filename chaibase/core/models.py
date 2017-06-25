from uuid import uuid4


from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import JSONField
from django.db.models import Model, UUIDField, CharField, DateTimeField, \
    ForeignKey, ManyToManyField, FloatField, BooleanField, DateField, \
    PositiveSmallIntegerField, Manager

from phonenumber_field.modelfields import PhoneNumberField
from django_google_maps.fields import AddressField, GeoLocationField

from chaibase.core.enums import EntryGrade, DeductionReason


class BaseManager(Manager):
    """
    Respect `is_deleted`
    """

    def everything(self):
        return super(BaseManager, self).get_queryset()

    def get_queryset(self):
        return self.everything().filter(is_deleted=False)

    def deleted_set(self):
        return self.everything().filter(is_deleted=True)


class BaseModel(Model):
    '''
    This shoud be inherited by all the classes whose objects are created due
    to user interaction.
    '''
    objects = BaseManager
    is_deleted = BooleanField(default=False)
    uuid = UUIDField(default=uuid4, primary_key=True, editable=False)

    class Meta:
        abstract = True

    def delete(self):
        """
        Override delete
        """
        self.is_deleted = True
        self.save()
        return self

    def undelete(self):
        """
        Override delete
        """
        self.is_deleted = False
        self.save()
        return self

    def __str__(self):
        return f"{self.uuid}, {self.is_deleted}"

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.__str__()}>'


class User(BaseModel, AbstractUser):
    '''
    A custom user so that we can add permissions easily
    '''
    socket_uuid = UUIDField(
        default=uuid4, editable=False, db_index=True, unique=True)
    phone_number = PhoneNumberField(blank=True)

    class Meta(AbstractUser.Meta):
        abstract = False
        unique_together = ('email',)

    def save(self, *args, **kwargs):
        if 'pbkdf2_sha256' not in self.password:
            self.set_password(self.password)
        self.username = self.username.lower()
        self.email = self.email.lower()
        super(User, self).save(*args, **kwargs)
        return self



class Location(BaseModel):
    '''
    Location Model
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
    location = ForeignKey(Location, related_name='factories', null=True)
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
    full_name = CharField(max_length=50, unique=True)
    home_number = PhoneNumberField(blank=True)
    mobile_number = PhoneNumberField(blank=True)
    office_number = PhoneNumberField(blank=True)
    location = ForeignKey(Location, related_name='people', null=True)

    def __str__(self):
        return self.full_name


class Weighment(BaseModel):
    date = DateField(default=now)
    person = ForeignKey(Person, related_name="weighments")
    vehicle = ForeignKey(Vehicle, related_name="weighments")
    factory = ForeignKey(Factory, related_name="weighments")
    entry_count = PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'f({self.factory}):p({self.person}):v({self.vehicle})'\
            f':d({self.date})'


class Entry(BaseModel):
    weight = FloatField(default=0.0)
    is_confirmed = BooleanField(default=False)
    weighment = ForeignKey(Weighment, related_name="entries")
    grade = PositiveSmallIntegerField(
        default=EntryGrade.UNKNOWN, choices=EntryGrade.CHOICES)

    def __str__(self):
        return f'w({self.weighment}):{self.weight}:{self.is_confirmed}'\
            f':{self.get_grade_display()}'


class Deduction(BaseModel):
    weight = FloatField(default=0.0)
    weighment = ForeignKey(Weighment, related_name="deductions")
    reason = PositiveSmallIntegerField(
        default=DeductionReason.UNKNOWN, choices=DeductionReason.CHOICES)

    def __str__(self):
        return f'w({self.weighment}):{self.weight}:{self.get_reason_display()}'
