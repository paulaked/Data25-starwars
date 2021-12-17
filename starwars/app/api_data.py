import requests
import json
from pprint import pprint


def get_api_url():
    # starwars = requests.get("https://www.swapi.tech/api/starships/")
    total_records = str(requests.get("https://www.swapi.tech/api/starships/").json()['total_records'])
    starwars = requests.get("https://www.swapi.tech/api/starships?page=1&limit=" + total_records)

    url_list = []
    for i in starwars.json()['results']:
        url_list.append(i['url'])

    return url_list


def create_starship_list():
    url_list = get_api_url()

    starship_list = []
    for i in url_list:
        starship_list.append((requests.get(i)).json()['result']['properties'])

    return starship_list
        # starship_name = (requests.get(i)).json()['result']['properties']['name']
        # file_name = starship_name + ".json"
        # with open(file_name, 'w') as jsonfile:
        #     json.dump((requests.get(i)).json()['result']['properties'], jsonfile, sort_keys=True, indent=4,
        #               ensure_ascii=False)


def find_pilot_id():
    starship_list = create_starship_list()
    for i in starship_list:
        if i['pilots']:
            for x in i['pilots']:

                #request pilot get name
                #search for name in characters get ObjectId
                #insert id into pilot
                #put into mongo


def return_pilot_id():

find_pilot_id()
