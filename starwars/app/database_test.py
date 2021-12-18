from pymongo import MongoClient

client = MongoClient()
db = client.starwars


#   test to check for valid mongodb connection
def test_pymongo_valid_instance():
    fail = False
    try:
        client.server_info()
    except:
        assert fail is True
    else:
        assert fail is False


