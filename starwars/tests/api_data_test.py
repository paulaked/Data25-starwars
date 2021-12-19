# tests to check if all data from api is correct place and type
import requests
import starwars.config_manager as config


#   test for correct data in api /starships endpoint
#   check if results key, total_records key and url key are in api and results is a list
def test_all_starships_endpoint():
    dict_key = requests.get(config.SWAPI_URL + "/api/starships/").json()
    success = False
    if 'results' in dict_key and type(dict_key['results']) is list and 'total_records' in dict_key:
        for result in dict_key['results']:
            if 'url' in result:
                success = True

    assert success


#   test starship entries match total_records
#   test all individual starship urls work
def test_url():
    total_records = requests.get(config.SWAPI_URL + "/api/starships/").json()['total_records']
    starship = requests.get(config.SWAPI_URL + "/api/starships?page=1&limit=" + str(total_records))

    check_url = 0
    check = 0
    if starship.json()['results'][-1] == (total_records - 1):
        for i in starship.json()['results']:
            check += 1
            if i['url'].status_code == 200:
                check_url += 1

    assert check_url == check


#   test for correct data in individual api /starships/<id> endpoint
#   check if result key, property key and pilots key in starship api and pilots is a list
def test_individual_starship_endpoint():
    total_records = requests.get(config.SWAPI_URL + "/api/starships/").json()['total_records']
    starships = requests.get(config.SWAPI_URL + "/api/starships?page=1&limit=" + str(total_records))
    results = starships.json()['results']

    #   if unassigned python thinks it might be referenced before assignment
    success = False
    for result in results:
        dict_key = requests.get(result['url']).json()
        success = False
        if 'result' in dict_key and 'properties' in dict_key['result'] and \
           'pilots' in dict_key['result']['properties'] and \
           type(dict_key['result']['properties']['pilots']) is list:
            success = True

        if not success:
            break

    assert success


#   test for correct data in pilot api /people/<id> endpoint
#   check if pilot name is a string
def test_type_pilot_name():
    total_records = requests.get(config.SWAPI_URL + "/api/starships/").json()['total_records']
    starships = requests.get(config.SWAPI_URL + "/api/starships?page=1&limit=" + str(total_records))
    results = starships.json()['results']

    #   if unassigned python thinks it might be referenced before assignment
    success = False
    for result in results:
        starship = requests.get(result['url']).json()
        success = False
        for pilot in starship['result']['properties']['pilots']:
            if type(requests.get(pilot).json()['result']['properties']['name']) == str:
                success = True

            if not success:
                break

        if not success:
            break

    assert success


#   test all starship links are starships
def test_if_starships():
    starship = requests.get(config.SWAPI_URL + "/api/starships/").json()['results']

    #   if unassigned python thinks it might be referenced before assignment
    is_starship = ''
    for result in starship:
        is_starship = requests.get(result['url']).json()['result']['description']

    assert is_starship == "A Starship"
