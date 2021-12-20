import requests
import pymongo
from upload_starships import insert_starships
from pilot_keys import insert_pilots
from create_collection import starships_collection


# Run this to upload starships from swapi, collate pilot information and create a starships
# collection in MongoDB

starships_collection(insert_pilots(insert_starships("https://www.swapi.tech/api/starships/")))