
if __name__ == '__main__':
    pass

import requests
import pymongo

client = pymongo.MongoClient()
db = client['starwars']


def get_api():
        #get total number of records from API
        starships = requests.get("https://www.swapi.tech/api/starships?page=1&1limit=36")
        urls = []

        #append results (starship urls) into list
        for i in starships.json()['results']:
            urls.append(i['url'])

        return urls


def get_starships():
        #url list from get_api function
        urls = get_api()
        all_starships = []
        
        #append starship values into list
        for i in urls:
        responses = requests.get(i).json()['result']['properties']
        print(responses)
        all_starships.append(responses)

        return all_starships


def return_pilot(name):
    char = db.characters.find_one({'name': name}, {'_id': 1})
    return char


def insert_id():
    starships = get_starships()
    for i in starships:
        if i['pilots']:
            for x in i['pilots']:
                pilot_id = return_pilot(requests.get(x).json()['result']['properties']['name'])
                starships[starships.index(i)]['pilots'][i['pilots'].index(x)] = pilot_id

    return starships


def insert_collection():
    #drop old collection, create new collection from starships and insert into mongodb
    db.drop_collection('starships')
    db.create_collection('starships')
    starships = insert_id()
    for i in starships:
        db.starships.insert_one(i)

    return


insert_collection()

