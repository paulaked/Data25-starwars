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


#   test to check if starwars database exists
def test_db_exists():
    assert 'starwars' in client.list_database_names()


