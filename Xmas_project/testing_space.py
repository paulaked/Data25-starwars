import pymongo

client = pymongo.MongoClient()  # opens connection to mongo deamon
db = client['starwars']