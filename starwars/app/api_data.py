import requests
import json
from pprint import pprint


def get_api_url():
    starwars = requests.get("https://www.swapi.tech/api/starships/")
    total_records = str(starwars.json()['total_records'])
    starwars = requests.get("https://www.swapi.tech/api/starships?page=1&limit=" + total_records)

    url_list = []
    for i in starwars.json()['results']:
        url_list.append(i['url'])

    return url_list


def create_json():
    url_list = get_api_url()
    # for i in url_list:
    #     with open():


print(create_json())
