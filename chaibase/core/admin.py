from django.contrib import admin

from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

from chaibase.core.models import User, Location, Factory, Person


class LocationAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {
            'widget': map_widgets.GoogleMapsAddressWidget},
    }


admin.site.register(User)
admin.site.register(Location, LocationAdmin)
admin.site.register(Factory)
admin.site.register(Person)
