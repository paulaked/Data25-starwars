import pymongo
import requests
import json
from pprint import pprint

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
    data = requests.get("https://www.swapi.tech/api/starships/").json()
    starships.append(data["results"])
    while data["next"]:
        data = requests.get(data["next"]).json()
        starships.append(data["results"])
    return starships


def replace_oids(data):
    # Extract the starship URLs which link to the pilot details.
    starship_details = []
    for item in data:
        for elements in item:
            starship_details.append(elements["url"])

    # Replace pilots with list of character OIDs.
    # replaced_data = []
    # for starship in starship_details:
    #     pilot_list = []
    #     for pilot in starship["pilots"]:
    #         name = requests.get(pilot).json()["result"]["properties"]["name"]
    #         pilot_id = db.characters.find_one({"name": name}, {"_id": 1})
    #         pilot_list.append(pilot_id)
    #     starship.update({'pilots': pilot_list})
    return starship_details


def insert_starships():
    # Insert starships into the database.
    db.create_collection("starships")


# --------------- EXTRA TESTS --------------- #
print("# ------------------ FUNCTION 1: DROP STARSHIPS ------------------ #")
drop_starships()
data1 = db.starships.find({})
for i in data1:
    print(i)

print("# ------------------ FUNCTION 2: PULL DATA ------------------ #")
data2 = pull_data()
for i in data2:
    print(i)

print("# ------------------ FUNCTION 3: REPLACE OBJECT IDS ------------------ #")
data3 = replace_oids(data2)
for i in data3:
    print(i)

print("# ------------------ FUNCTION 4: INSERT DATA ------------------ #")
insert_starships()
data4 = db.starships.find({})
for i in data4:
    print(i)
