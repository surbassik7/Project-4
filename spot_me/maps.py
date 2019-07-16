
import googlemaps
import json
import pprint
# import requests


# Define the API Key.
API_KEY = 'AIzaSyDOwVK7bGap6b5Mpct1cjKMp7swFGi3uGg'

# Define the Client
gmaps = googlemaps.Client(key = API_KEY)

# Do a simple nearby search where we specify the location
# in lat/lon format, along with a radius measured in meters
