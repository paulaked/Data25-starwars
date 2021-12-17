import pymongo
import requests

client = pymongo.MongoClient()
db = client["starwars"]


def drop_starships():
    # If entries in the database exist, then drop them.
    if db.starships.find({}) != "":
        db.starships.delete_many({})
    # Otherwise, proceed as normal.


def pull_data():
    # Get all data from SWAPI.
    pass


def replace_oids():
    # Replace pilots with list of OIDs from Characters.
    pass


def insert_starships():
    # Insert starships into the database.
    pass


# --------------- EXTRA TESTS --------------- #

drop_starships()
testing1 = db.starships.find({})
for i in testing1:
    print(i)
