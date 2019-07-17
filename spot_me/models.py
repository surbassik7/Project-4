from django.db import models
from django_google_maps import fields as map_fields
import django.contrib.gis.db.models as gis_models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=1000)
    photo_url = models.TextField()

    def __str__(self):
        return self.name

class Gym(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Search(models.Model):
    term = models.CharField(max_length=255, null=True, blank=True)
    position = gis_models.PointField(srid=4326, dim=2)
    results_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} ({})".format(self.term, self.position)


from django.db import models

    