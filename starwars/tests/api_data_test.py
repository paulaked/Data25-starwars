import requests


def test_url():
    check = requests.get("https://www.swapi.tech/api/starships/")
    assert check.status_code == 200

