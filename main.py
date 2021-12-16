#import the starships data from the api
import requests
import pymongo
from pprint import pprint

starship_request = requests.get("https://www.swapi.tech/api/starships/")

starships = starship_request.json()
print(starships)



