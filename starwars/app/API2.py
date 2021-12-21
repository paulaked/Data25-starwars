import requests
# import json
import pymongo

client = pymongo.MongoClient()
db = client['starwars']


def get_api():
    # star_wars = requests.get("https://www.swapi.tech/api/starships/")    # find total number of records in API
    all_records = str(requests.get("https://www.swapi.tech/api/starships/").json()['all_records'])
    # concantenate total records to show all starships on one page
    star_wars = requests.get("https://www.swapi.tech/api/starships?page=1&limit=" + all_records)

    urls = []
    # appending the 'results' values (individual starship urls) into a list
    for i in star_wars.json()['results']:
        urls.append(i['url'])

    return urls


def create_starships():
    # get url list from get_api function
    urls = get_api()

    starships = []
    # appending the starship properties values from url list into a list
    for i in urls:
        starships.append((requests.get(i)).json()['result']['properties'])

    return starships


def return_pilot(name):
    char = db.characters.find_one({'name': name}, {'_id': 1})
    return char


def insert_id():
    starships = create_starships()
    for i in starships:
        if i['pilots']:
            for x in i['pilots']:
                pilot_id = return_pilot(requests.get(x).json()['result']['properties']['name'])
                starships[starships.index(i)]['pilots'][i['pilots'].index(x)] = pilot_id

    return starships


def insert_collection():
    # drop collection
    db.drop_collection('starships')
    # create collection
    db.create_collection('starships')
    # get starship list with pilot id
    starships = insert_id()
    # insert starships to collection from list
    for i in starships:
        db.starships.insert_one(i)

    return


insert_collection()

