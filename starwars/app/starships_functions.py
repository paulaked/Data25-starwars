import requests
import pprint
import json
from itertools import chain
import pymongo

# set up pymongo
client = pymongo.MongoClient()
db = client['starwars']



def get_raw_starships():
    starship_requests_raw = requests.get("https://www.swapi.tech/api/starships/")
    #print(starship_requests_raw.status_code)
    #pprint.pprint(starship_requests.json())
    starships_count = str(starship_requests_raw.json()['total_records'])  # identifies 36 starships
    # returns starships_count and so identifies number of urls to scrape
    url_list = []
    starships_urls = requests.get(f"https://www.swapi.tech/api/starships?page=1&limit={starships_count}")
    for url in starships_urls.json()['results']:
        url_list.append(url['url'])  #returns a list of urls containing the starship data
    return url_list
    
# pprint.pprint(get_raw_starships())

def get_relavent_info():
    starship_data = []
    for url in get_raw_starships():
        starship_data.append(requests.get(url).json()['result']['properties']) 
    return starship_data
    # returns json containing information in the 'properties' category

# pprint.pprint(get_relavent_info())

def get_pilots_in_list():
    new_starship_pilot_data = []
    starship_data = get_relavent_info()
    for starship in starship_data:
        if starship['pilots'] ==[]:
            continue
        else:
            starship_pilots = starship['pilots']
            pilot_list = []
            for pilot in starship_pilots:
                pilot_name = requests.get(pilot).json()['result']['properties']['name']
                pilot_id_from_characters = db.characters.find_one({"name": pilot_name}, {"_id": 1})
                pilot_list.append(pilot_id_from_characters)
            starship['pilots'] = pilot_list
            starship.update({'pilots': pilot_list})
        new_starship_pilot_data.append(starship)
    return new_starship_pilot_data

pprint.pprint(get_pilots_in_list())







