from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=1000)
    photo_url = models.TextField()

    def __str__(self):
        return self.name

class Gym(models.Model):
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=1000)