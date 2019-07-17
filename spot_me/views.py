from django.shortcuts import render
from .models import User, Gym
from googlemaps import Client
gmaps = Client(key='A')
# Create your views here.
