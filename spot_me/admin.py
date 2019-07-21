from django.contrib import admin
from .models import User, Gym
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from django.contrib.gis.admin import OSMGeoAdmin

from spot_me.models import Gym
from django.contrib import admin


# Register your models here.
@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'address', 'created_at', 'modified_at')

admin.register(Gym, GymAdmin)