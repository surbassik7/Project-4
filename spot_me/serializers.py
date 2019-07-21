from spot_me.models import Gym
from rest_framework import serializers


class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = ('id', 'name', 'address', 'location', 'photo', 'vicinity', 'phone number' 'hours of operation', 'website', 'review')