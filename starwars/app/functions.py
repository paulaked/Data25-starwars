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

#get starships' data from api data, stored in an array
def get_starships():
    ship_data = []
    for i in get_starship_data():
        dummyvar = requests.get(i["url"])
        dummyvar1 = dummyvar.json()

        ship_data.append(dummyvar1["result"]["properties"])
    return ship_data

#get pilot urls from api data, stored in an array
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

db.drop_collection("starships")
db.create_collection("starships")

#put starships data into starships collection: if a ship have no pilot, id field will be N/A, else list all pilot ids.
def fill_starships():
    ship_data = get_starships()
    pilots_url = get_pilot_url()
    id_array = get_pilot_id()
    for i in range(0, len(pilots_url) - 1):
        if not pilots_url[i]:
            db.starships.insert_one({
                "model": ship_data[i]['model'],
                "starship_class": ship_data[i]['starship_class'],
                "manufacturer": ship_data[i]['manufacturer'],
                "cost_in_credits": ship_data[i]['cost_in_credits'],
                "length": ship_data[i]['length'],
                "crew": ship_data[i]['crew'],
                "passengers": ship_data[i]['passengers'],
                "max_atmosphering_speed": ship_data[i]['max_atmosphering_speed'],
                "hyperdrive_rating": ship_data[i]['hyperdrive_rating'],
                "MGLT": ship_data[i]['MGLT'],
                "cargo_capacity": ship_data[i]['cargo_capacity'],
                "consumables": ship_data[i]['consumables'],
                "pilots": "N/A",
                "created": ship_data[i]['created'],
                "edited": ship_data[i]['edited'],
                "name": ship_data[i]['name'],
                "url": ship_data[i]['url'],
            })
        else:
            db.starships.insert_one({
                "model": ship_data[i]['model'],
                "starship_class": ship_data[i]['starship_class'],
                "manufacturer": ship_data[i]['manufacturer'],
                "cost_in_credits": ship_data[i]['cost_in_credits'],
                "length": ship_data[i]['length'],
                "crew": ship_data[i]['crew'],
                "passengers": ship_data[i]['passengers'],
                "max_atmosphering_speed": ship_data[i]['max_atmosphering_speed'],
                "hyperdrive_rating": ship_data[i]['hyperdrive_rating'],
                "MGLT": ship_data[i]['MGLT'],
                "cargo_capacity": ship_data[i]['cargo_capacity'],
                "consumables": ship_data[i]['consumables'],
                "pilots": {"_id": id_array[i]},
                "created": ship_data[i]['created'],
                "edited": ship_data[i]['edited'],
                "name": ship_data[i]['name'],
                "url": ship_data[i]['url'],
            })



