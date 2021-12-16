from pprint import pprint
import requests
import json
import pymongo
if __name__ == '__main__':
    pass


def get_from_api():
    responses = []
    response = requests.get('https://www.swapi.tech/api/starships/').json()
    responses += response['results']
    while response['next'] is not None:
        response = requests.get(response['next']).json()
        responses += response['results']
    return responses


def collect_starships():
    starships = []
    for i in get_from_api():
        starships.append(requests.get(i['url']).json()['result']['properties'])
    return starships


def collect_pilots():
    starships = []
    for starship in collect_starships():
        pilots = []
        for pilot in starship['pilots']:
            pilots.append(requests.get(pilot).json()['result']['properties']['name'])
        starship.update({'pilots': pilots})
        starships.append(starship)
    return starships


