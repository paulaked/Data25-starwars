from starships_functions import *
import pprint
import pytest

# placeholder comment


# Test 1: Check API response

def test_api_response():
    check = requests.get("https://www.swapi.tech/api/starships/")
    assert check.status_code == 200



# Test 2: Check to see whether the get_relevant_info() function has actually returned data:

def test_relevant_info_existence():
    test_data = get_relevant_info()
    assert any(test_data)


# Test 3: Check to see whether URLs in [Pilots] have been replaced with character object IDs - done by investigating the "A-wing" entry:

def test_objectids_in_data():
    test_data = get_pilots_in_list()
    flag = False
    for starship in test_data:
        if starship['name'] == "A-wing" and "ObjectID" in test_data['Pilots']:
            flag = True
    assert flag


# Test 4: Check to see whether starships data has made it to the MongoDB database

def test_data_in_db():
    add_collection_to_database()
    assert any(db.starships.find({}))