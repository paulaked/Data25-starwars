from starwars.app.functions import *
import validators

def test_get_api_data():
    assert get_api_data().status_code is 200

def test_to_json():
    assert type(to_json()) is dict

def test_get_starship_data():
    for i in get_starship_data():
        assert type(i) is dict

def test_get_starship():
    for i in get_starships():
        assert type(i) is dict

def test_get_pilot_url():
    for i in get_pilot_url():
        if not i:
            continue
        else:
            for j in i:
                assert validators.url(j) is True

def test_get_pilot_id():
    for i in get_pilot_id():
        if not i:
            continue
        else:
            for j in i:
                assert int(j, 16) is True


