import pymongo

client = pymongo.MongoClient()
db = client['starwars']


#   takes a name argument as a string finding a match in the characters collection of the starwars database
#   returns the matched characters id as a dictionary key, value
def return_pilot_id(name):
    if name is not str:
        raise TypeError('Work only with strings')
    char_id = db.characters.find_one({'name': name}, {'_id': 1})
    return char_id
