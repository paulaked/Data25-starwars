#check if all locations are correct type; dict string url name
#results and properties
import requests


def test_for_url():
    total_records = str(requests.get("https://www.swapi.tech/api/starships/").json()['total_records'])
    star_wars = requests.get("https://www.swapi.tech/api/starships?page=1&limit=" + total_records)

    check_url = 0
    check = 0
    for i in star_wars.json()['results']:
        check += 1
        if i.status_code == 200:
            check_url += 1

    assert check_url == check

