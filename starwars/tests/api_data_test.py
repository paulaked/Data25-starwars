# tests to check if all data from api is correct place and type
import requests
import starwars.config_manager as config


#   test for correct data in api /starships endpoint
#   check if results key, total_records key and url key are in api and results is a list
#passed
def test_all_starships_endpoint():
    dict_key = requests.get(f"{config.SWAPI_URL}/api/starships/").json()
    success = False
    if 'results' in dict_key and type(dict_key['results']) is list and 'total_records' in dict_key:
        for result in dict_key['results']:
            if 'url' in result:
                success = True
            else:
                success = False
                break

    assert success


#   test starship entries match total_records
#   test all individual starship urls work
#passed
def test_url():
    total_records = requests.get(f"{config.SWAPI_URL}/api/starships/").json()['total_records']
    starship = requests.get(f"{config.SWAPI_URL}/api/starships?page=1&limit={str(total_records)}")

    success = False
    if starship.json()['results'].index(starship.json()['results'][-1]) == (total_records - 1):
        for i in starship.json()['results']:
            if i['url']:
                if requests.get(i['url']).status_code == 200:
                    success = True
                else:
                    success = False
                    break

    assert success


#   test for correct data in individual api /starships/<id> endpoint
#   check if result key, property key and pilots key in starship api and pilots is a list
#passed
def test_individual_starship_endpoint():
    total_records = requests.get(f"{config.SWAPI_URL}/api/starships/").json()['total_records']
    starships = requests.get(f"{config.SWAPI_URL}/api/starships?page=1&limit={str(total_records)}")
    results = starships.json()['results']

    #   if unassigned python thinks it might be referenced before assignment
    success = False
    for result in results:
        dict_key = requests.get(result['url']).json()
        if 'result' in dict_key and 'properties' in dict_key['result'] and \
           'pilots' in dict_key['result']['properties'] and \
           type(dict_key['result']['properties']['pilots']) is list:
            success = True
        else:
            success = False
            break

    assert success


#   test for correct data in pilot api /people/<id> endpoint
#   check if pilot name is a string
#passed
def test_type_pilot_name():
    total_records = requests.get(f"{config.SWAPI_URL}/api/starships/").json()['total_records']
    starships = requests.get(f"{config.SWAPI_URL}/api/starships?page=1&limit={str(total_records)}")
    results = starships.json()['results']

    #   if unassigned python thinks it might be referenced before assignment
    success = False
    for result in results:
        starship = requests.get(result['url']).json()
        if starship['result']['properties']['pilots']:
            for pilot in starship['result']['properties']['pilots']:
                if type(requests.get(pilot).json()['result']['properties']['name']) is str:
                    success = True
                else:
                    success = False
                    break
            if not success:
                break

    assert success


#   test all starship links are starships
#passed
def test_if_starships():
    starship = requests.get(f"{config.SWAPI_URL}/api/starships/").json()['results']

    #   if unassigned python thinks it might be referenced before assignment
    is_starship = ''
    for result in starship:
        is_starship = requests.get(result['url']).json()['result']['description']

    assert is_starship == "A Starship"
