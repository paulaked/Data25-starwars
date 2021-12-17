import requests
import pymongo
from upload_starships import insert_starships
from pilot_keys import insert_pilots

client = pymongo.MongoClient()
db = client['starwars']


def starships_collection(starships_list):
    db.create_collection("starships")
    for starship in starships_list:
        db.starships.insert_one(starship)


starships_collection(insert_pilots(insert_starships("https://www.swapi.tech/api/starships/")))