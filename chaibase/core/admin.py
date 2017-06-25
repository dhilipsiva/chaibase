from django.contrib import admin

from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

from chaibase.core.models import User, Location, Factory, Person, Vehicle, \
    Weighment, Entry, Deduction, Browser


class BaseAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_deleted',)
    list_filter = ('is_deleted',)


class LocationAdmin(BaseAdmin):
    formfield_overrides = {
        map_fields.AddressField: {
            'widget': map_widgets.GoogleMapsAddressWidget},
    }


admin.site.register(User, BaseAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Factory, BaseAdmin)
admin.site.register(Person, BaseAdmin)
admin.site.register(Vehicle, BaseAdmin)
admin.site.register(Weighment, BaseAdmin)
admin.site.register(Entry, BaseAdmin)
admin.site.register(Deduction, BaseAdmin)

admin.site.register(Browser)
