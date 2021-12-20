from starwars.app.return_pilot_id import return_pilot_id
import pymongo

client = pymongo.MongoClient()
db = client['starwars']


def test_check_correct_char():
    char_id = return_pilot_id('Darth Vader')
    flag = False
    if char_id == f"{{\'_id\': ObjectId(\'61ba18a925cfc799b15fafa5\')}}":
        flag = True

    assert flag


def test_value_error():
    try:
        return_pilot_id('0')
    except ValueError as ve:
        assert True
