import pymongo

# Setup of pymongo
client = pymongo.MongoClient()
db = client['starwars']


# starships_collection is a function that takes the list created in pilot_keys
# and creates a starships collection in MongoDB
def starships_collection(starships_list):
    db.create_collection("starships")

    for starship in starships_list:
        db.starships.insert_one(starship)
