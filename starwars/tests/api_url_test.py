# tests to check if starships api endpoints work
import requests
import starwars.config_manager as config


def test_url():
    check = requests.get(f"{config.SWAPI_URL}/api/starships/")
    assert check.status_code == 200


def test_starship_all_url():
    total_records = str(requests.get(f"{config.SWAPI_URL}/api/starships/").json()['total_records'])
    star_wars = requests.get(f"{config.SWAPI_URL}/api/starships?page=1&limit={total_records}")
    assert star_wars.status_code == 200
