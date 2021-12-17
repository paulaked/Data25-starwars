import requests
import pymongo
from upload_starships import insert_starships
from pilot_keys import insert_pilots


def starships_collection(starships_list):
    db.create_collection("starships")
