import pymongo
import requests

client = pymongo.MongoClient()
db = client["starwars"]


def drop_starships():

    # If entries in the database exist, then drop them.
    if db.starships.find({}) != "":
        db.starships.delete_many({})
    # Otherwise, proceed as normal.


# EXTRA TESTS #

drop_starships()
testing1 = db.starships.find({})
for i in testing1:
    print(i)

