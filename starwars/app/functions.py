import requests
import json
import pymongo

#connect to Mongodb and create collection
client = pymongo.MongoClient()
db = client['starships']

#access api and store starship data
def get_api_data():
    tol_records = str(requests.get("https://www.swapi.tech/api/starships/").json()['total_records'])
    api_data = requests.get("https://www.swapi.tech/api/starships?page=1&limit=" + tol_records)
    return api_data

#convert api_data into json format
def to_json():
    return get_api_data().json()

#get only starships data from json file
def get_starship_data():
    return to_json()['results']


