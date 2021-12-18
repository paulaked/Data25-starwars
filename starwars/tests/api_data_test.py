# tests to check if all data from aip is correct type

import requests

#   test for correct data in api /starships endpoint
def test_all_starships_endpoint():
    dict_key = requests.get("https://www.swapi.tech/api/starships/").json()['total_records']
    is_true = False
    if 'results' in dict_key:
        if type(dict_key['results']) == list:
            for i in dict_key['results']:
                if 'url' in dict_key['results']:
                    is_true = True

    assert is_true is True


#   test all individual starship urls are correct
def test_url():
    total_records = str(requests.get("https://www.swapi.tech/api/starships/").json()['total_records'])
    starship = requests.get("https://www.swapi.tech/api/starships?page=1&limit=" + total_records)

    check_url = 0
    check = 0
    for i in starship.json()['results']:
        check += 1
        if i['url'].status_code == 200:
            check_url += 1

    assert check_url == check


#   test all starship links are starships
def test_if_starships():
    first_starship = requests.get("https://www.swapi.tech/api/starships/").json()['results'][0]['url']
    is_starship = requests.get(first_starship).json()['result']['description']

    assert is_starship == "A Starship"
