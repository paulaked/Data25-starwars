import requests
import json
from pprint import pprint

# Retrieve starwars api data from swapi
# Convert api to json format
response1 = requests.get('https://swapi.dev/api/starships/').json()
response2 = requests.get(response1['next']).json()
response3 = requests.get(response2['next']).json()
response4 = requests.get(response3['next']).json()

pprint(response1)
pprint(response1)
pprint(response1)
pprint(response1)