# import requests
import googlemaps
import json
import pprint

# Define the API Key.
API_KEY = ''

# Define the Client
gmaps = googlemaps.Client(key = API_KEY)



# Do a simple nearby search where we specify the location
# in lat/lon format, along with a radius measured in meters
