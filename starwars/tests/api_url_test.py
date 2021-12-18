import requests


def test_url():
    check = requests.get("https://www.swapi.tech/api/starships/")
    assert check.status_code == 200

def test_starship_all_url():
    total_records = str(requests.get("https://www.swapi.tech/api/starships/").json()['total_records'])
    star_wars = requests.get("https://www.swapi.tech/api/starships?page=1&limit=" + total_records)
    assert star_wars.status_code == 200
