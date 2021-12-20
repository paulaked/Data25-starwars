import pymongo
import requests

# Setup of pymongo
client = pymongo.MongoClient()
db = client['starwars']


# insert_pilots is a function that finds the pilot name from the pilot url and inserts
# a pymongo function that will insert the pilot ID when the collection in made in MongoDB
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


