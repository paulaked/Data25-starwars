from upload_starships import insert_starships
import pymongo
import requests
import pprint as pp

client = pymongo.MongoClient()
db = client['starwars']


def insert_pilots(starships_list):
    for ship in starships_list:
        if ship['pilots'] == []:
            ship['pilots'] = 'No pilots'
        else:
            pilots = ship['pilots']
            pilot_list = []
            for pilot in pilots:
                pilot_name = requests.get(pilot).json()['result']['properties']['name']
                pilot_info = db.characters.find_one({"name": pilot_name}, {"_id": 1})
                pilot_list.append(pilot_info)
            ship['pilots'] = pilot_list

    return starships_list

# pp.pprint(insert_pilots(insert_starships("https://www.swapi.tech/api/starships/")))
