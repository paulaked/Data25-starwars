import pymongo

client = pymongo.MongoClient()
db = client['starwars']


def return_pilot_id(name):
    char_id = db.characters.find_one({'name': name}, {'_id': 1})
    return char_id
