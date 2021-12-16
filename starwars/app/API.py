import requests
import json
from pprint import pprint

def get_api_url():
    starwars = requests.get("https://www.swapi.tech/api/starships/")
    total_records = str(starwars.json()['total_records'])
    starwars= requests.get("https://www.swapi.tech/api/starships?page=1&limit=" + total_records)

    url_results = []

    for i in starwars.json()['results']:
        url_results.append(i['url'])

    return url_results

print(get_api_url())

def create_json(url_list):
    url_list = get_api_url()
    return url_list

print(create_json())
