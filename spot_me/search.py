import json
import requests
import googlemaps
from googlemaps import Client

check_url = 'http://api.ipstack.com/check?access_key=3fea3b33a38ef7abd674c9e0515183be'
r = requests.get(check_url)
j = json.loads(r.text)
lat = j['latitude']
lon = j['longitude']
mylocation = (','.join([str(lat), str(lon)]))

print(mylocation)


BASE_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
LOCATION = mylocation
RADIUS = '2500'
TYPE = 'gym'
API_KEY = 'AIzaSyDOwVK7bGap6b5Mpct1cjKMp7swFGi3uGg'
KEYWORDS = ''

allgyms = requests.get(BASE_URL+'location='+LOCATION+'&radius='+RADIUS+'&type='+TYPE+'&key='+API_KEY)
all_text = allgyms.text
alljson = json.loads(all_text)

KEYWORDS = 'healthclub'
healthclubs = requests.get(BASE_URL+'location='+LOCATION+'&radius='+RADIUS+'&type='+TYPE+'&keyword='+KEYWORDS+'&key='+API_KEY) 
health_text = healthclubs.text 
healthjson = json.loads(health_text)


KEYWORDS = 'crossfit'
crossfit = requests.get(BASE_URL+'location='+LOCATION+'&radius='+RADIUS+'&type='+TYPE+'&keyword='+KEYWORDS+'&key='+API_KEY) 
cross_text = crossfit.text 
crossjson = json.loads(cross_text)


KEYWORDS = '(martial) AND (arts)'
martialarts = requests.get(BASE_URL+'location='+LOCATION+'&radius='+RADIUS+'&type='+TYPE+'&keyword='+KEYWORDS+'&key='+API_KEY) 
martial_text = martialarts.text 
martialjson = json.loads(martial_text)


KEYWORDS = '(yoga) AND (pilates)'
yoga = requests.get(BASE_URL+'location='+LOCATION+'&radius='+RADIUS+'&type='+TYPE+'&keyword='+KEYWORDS+'&key='+API_KEY) 
yoga_text = yoga.text 
yogajson = json.loads(yoga_text)


print(crossjson)