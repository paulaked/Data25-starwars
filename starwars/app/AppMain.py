import pymongo
import requests

client = pymongo.MongoClient()
db = client["starwars"]


def drop_starships():
    # If entries in the database exist, then drop them just to be sure.
    if db.starships.find({}) != "":
        db.starships.delete_many({})
    # Now drop the entire collection.
    db.starships.drop()


def pull_data():
    # Get starships data from SWAPI.
    starships = []
    data = requests.get("https://www.swapi.tech/api/starships/").json()
    starships.append(data["results"])
    while data["next"]:
        data = requests.get(data["next"]).json()
        starships.append(data["results"])
    return starships


def replace_oids():
    # Extract the starship URLs which link to the pilot details.
    starship_details = []
    for item in pull_data():
        for elements in item:
            starship_details.append(requests.get(elements["url"]).json()["result"]["properties"])

    # Replace pilot URLs with list of character OIDs.
    replaced_data = []
    for starship in starship_details:
        pilot_list = []
        for pilot in starship["pilots"]:
            # Find the pilot's name and search characters db to find their ObjectID.
            name = requests.get(pilot).json()["result"]["properties"]["name"]
            pilot_id = db.characters.find_one({"name": name}, {"_id": 1})
            pilot_list.append(pilot_id)
        starship.update({'pilots': pilot_list})
        replaced_data.append(starship)
    return replaced_data


def insert_starships():
    # Insert starships into the database.
    drop_starships()
    db.create_collection("starships")
    for item in replace_oids():
        # Clause to avoid inserting any pilots section for empty entries.
        if not item["pilots"]:
            del item["pilots"]
        db.starships.insert_one(item)


# --------------- EXTRA TESTS --------------- #

print("#*-*-*-*-*-*-*-*-*-*-* STARTING PROGRAM *-*-*-*-*-*-*-*-*-*-*")
insert_starships()
data4 = db.starships.find({})
print("*-*-*-*-*-*-*-*-*-*-* PRINTING RESULT *-*-*-*-*-*-*-*-*-*-*")
for i in data4:
    print(i)
