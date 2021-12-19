import pymongo
from app.get_name_insert_id import get_name_insert_id

client = pymongo.MongoClient()
db = client['starwars']


#   Function creates starship collection inserts starship data into collection
def drop_create_insert_collection():
    # drop collection
    db.drop_collection('starships')
    # create collection
    db.create_collection('starships')
    # get starship list with pilot id
    starship_list = get_name_insert_id()
    # insert starships to collection from list
    for starship in starship_list:
        db.starships.insert_one(starship)

    return
