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
    # Get starships data from SWAPI.
    starships = []
    data = requests.get("https://www.swapi.tech/api/starships").json()
    starships.append(data["results"])
    while data["next"]:
        data = requests.get(data["next"]).json()
        starships.append(data["results"])
    return starships


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

data2 = pull_data()
for i in data2:
    print(i)
