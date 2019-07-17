from django.contrib import admin
from .models import User, Gym
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

class GymAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }


# Register your models here.
admin.site.register(User)
admin.site.register(Gym)