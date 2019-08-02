from django.contrib.gis import admin as gis_admin
from django.contrib import admin
from spot_me import models as spot_me_models


admin.site.register(spot_me_models.Search, gis_admin.GeoModelAdmin)
