from starwars.app.get_name_insert_id import get_name_insert_id
import pymongo

client = pymongo.MongoClient()
db = client['starwars']


def test_correct_pilot_id():
    starship_data_list = get_name_insert_id()
    flag = False
    # swap for: db.characters.find_one({'name': 'Darth Vader'}, {'_id': 1})
    pilot_id = f"{{\'_id\': ObjectId(\'61ba18a925cfc799b15fafa5\')}}"
    for i in starship_data_list:
        if i['name'] == "TIE Advanced x1" and pilot_id in starship_data_list['pilots']:
            flag = True

    assert flag


def test_empty_pilot_list():
    starship_data_list = get_name_insert_id()
    empty = False
    for i in starship_data_list:
        if not i['pilots'] and i['name'] == "Death Star":
            empty = True

    assert empty


def test_pilot_number():
    starship_data_list = get_name_insert_id()
    flag = False
    for i in starship_data_list:
        if i['name'] == "Millennium Falcon" and len(i['pilots']) == 4:
            flag = True

    assert flag
