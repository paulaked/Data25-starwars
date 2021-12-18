# tests to check if all data from aip is correct type

import requests

#   test all individual starship urls are correct
def test_for_url():
    total_records = str(requests.get("https://www.swapi.tech/api/starships/").json()['total_records'])
    starship = requests.get("https://www.swapi.tech/api/starships?page=1&limit=" + total_records)

    check_url = 0
    check = 0
    for i in starship.json()['results']:
        check += 1
        if i.status_code == 200:
            check_url += 1

    assert check_url == check


#   test all starship links are starships
def test_for_starships():
    first_starship = requests.get("https://www.swapi.tech/api/starships/").json()['results'][0]['url']
    is_starship = requests.get(first_starship).json()['result']['description']

    assert is_starship == "A Starship"
