from starwars.app.functions import *

def test_get_api_data():
    assert get_api_data().status_code is 200

def test_to_json():
    assert type(to_json()) is dict

def test_get_starship_data():
    for i in get_starship_data():
        assert type(i) is dict

