from pprint import pprint
import requests
import json
import pymongo
import os
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


def store_data():
    try:
        os.mkdir('starships')
    except FileExistsError:
        print('starships already exists')
    for starship in collect_pilots():
        file_name = os.path.join('starships', str(starship['name']) + '.json')
        with open(file_name, 'w') as json_file:
            json.dump(starship, json_file)


client = pymongo.MongoClient()
db = client['starwars']


def load_data():
    db['starships'].drop()
    starships = db['starships']
    for i in os.listdir('starships'):
        file_name = os.path.join('starships', i)
        with open(file_name, 'r') as json_file:
            starship = json.load(json_file)
        db.starships.insert_one(starship)


def references_pilot():
    starships = db.starships.find({})
    for starship in starships:
        pilots = [{}]
        for pilot in starship['pilots']:
            key = db.characters.find_one({'name': pilot})['_id']
            reference = {'_id': key}
            pilots.append(reference)
        db.starships.update_one({'name': starship['name']}, {'$set': {'pilots': pilots}})
