import json
import requests
import googlemaps
from googlemaps import Client

locationrequest = requests.get('http://api.ipstack.com/check?access_key=3fea3b33a38ef7abd674c9e0515183be&fields=latitude,longitude')
location_text = locationrequest.text
location = json.loads(location_text)
print(location)


gmaps = Client(key='AIzaSyDOwVK7bGap6b5Mpct1cjKMp7swFGi3uGg')

list_all_gyms = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/output?parameters')
print(list_all_gyms)