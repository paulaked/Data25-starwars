import requests
from create_starship_list import create_starship_list
from return_pilot_id import return_pilot_id


def get_name_insert_id():
    starship_list = create_starship_list()
    for i in starship_list:
        if i['pilots']:
            for x in i['pilots']:
                pilot_id = return_pilot_id(requests.get(x).json()['result']['properties']['name'])
                starship_list[starship_list.index(i)]['pilots'][i['pilots'].index(x)] = pilot_id

    return starship_list
