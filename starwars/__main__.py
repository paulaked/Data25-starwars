import requests
import json
import pymongo
from pprint import pprint

client = pymongo.MongoClient()
db = client['starwars']

if __name__ == '__main__':
    pass  # Replace this with code to run your app

# import the starships data from the api


# requesting the data from the api
starship_request1 = requests.get("https://www.swapi.tech/api/starships/")
# starship_request2 = requests.get("https://www.swapi.tech/api/starships?page=2&limit=10")
# starship_request3 = requests.get("https://www.swapi.tech/api/starships?page=3&limit=10")
# starship_request4 = requests.get("https://www.swapi.tech/api/starships?page=4&limit=10")

# converting them to json files
starships1 = starship_request1.json()
starships2 = starship_request2.json()
starships3 = starship_request3.json()
starships4 = starship_request4.json()

