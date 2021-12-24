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

#get starships' data and pilot urls from api data, stored in arrays
def get_pilot_url():
    pilots_url = []
    ship_data = []
    for i in get_starship_data():
        dummyvar = requests.get(i["url"])
        dummyvar1 = dummyvar.json()

        ship_data.append(dummyvar1["result"]["properties"])
        pilots_url.append(dummyvar1["result"]["properties"]["pilots"])
    return pilots_url

#get pilot name from urls, match names with id using data in charaters collection, store id in an array
def get_pilot_id():
    id_array = get_pilot_url()

    for i in range(0, len(id_array) - 1):
        for j in range(0, len(id_array[i])):
            dummyvar = requests.get(id_array[i][j])
            dummyvar1 = dummyvar.json()
            pilot_name = dummyvar1["result"]['properties']['name']
            pilot_id = db.charaters.find({"name": pilot_name}, {"_id": 1})
            for k in pilot_id:
                id_array[i][j] = str(k['_id'])
    return id_array


