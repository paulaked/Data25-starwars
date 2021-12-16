from pprint import pprint
import requests
import json
import pymongo
import os


def get_from_api():  # fetches data about the starships from teh API
    responses = []
    response = requests.get('https://www.swapi.tech/api/starships/').json()
    responses += response['results']
    while response['next'] is not None:  # ensures that all data is collected
        response = requests.get(response['next']).json()  # collects the link to the next page
        responses += response['results']  # adds information about the starships to the responses list
    return responses


def collect_starships():
    starships = []
    for starship in get_from_api():
        starships.append(requests.get(starship['url']).json()['result']['properties'])
        # uses the API to collect additional data
    return starships


def collect_pilots():
    starships = []
    for starship in collect_starships():
        pilots = []
        for pilot in starship['pilots']:
            pilots.append(requests.get(pilot).json()['result']['properties']['name'])
            # collects the name for all listed pilots
        starship.update({'pilots': pilots})  # replaces the pilot list with a list of character names
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
            json.dump(starship, json_file)  # stores the data for all starships into an individual JSON file


client = pymongo.MongoClient()
db = client['starwars']


def load_data():
    db['starships'].drop()
    starships = db['starships']  # drops the collection 'starships' then creates it again
    for file in os.listdir('starships'):
        file_name = os.path.join('starships', file)
        with open(file_name, 'r') as json_file:
            starship = json.load(json_file)
        db.starships.insert_one(starship)    # loads the data into the starship collection in MongoDB


def references_pilot():
    starships = db.starships.find({})
    for starship in starships:
        pilots = [{}]
        for pilot in starship['pilots']:
            key = db.characters.find_one({'name': pilot})['_id']
            # collects the object id for the pilots based on their name
            reference = {'_id': key}
            pilots.append(reference)
        db.starships.update_one({'name': starship['name']}, {'$set': {'pilots': pilots}})
        # replaces the pilot field with a document containing the pilot's object id for every pilot
