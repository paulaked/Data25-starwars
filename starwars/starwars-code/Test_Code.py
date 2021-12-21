import requests
import pymongo
from pprint import pprint

client = pymongo.MongoClient()
db = client['starwars']

starship_request1 = requests.get("https://www.swapi.tech/api/starships")
starship_request2 = requests.get('https://www.swapi.tech/api/starships?page=2&limit=10')
starship_request3 = requests.get('https://www.swapi.tech/api/starships?page=3&limit=10')
starship_request4 = requests.get('https://www.swapi.tech/api/starships?page=4&limit=10')

starships1 = starship_request1.json()
starships2 = starship_request2.json()
starships3 = starship_request3.json()
starships4 = starship_request4.json()
starshipsjsons = [starships1, starships2, starships3, starships4]
# pprint(starshipsjsons)

# VARIABLES
starships_names = []
starships_url = []
starships_info = []
pilot_urls_with_empties = []
pilot_info = []
pilot_names = []
pilot_url_without_empties = []
pilot_urls_ind = []


def collecting_starships_and_pilots():
    for x in range(0, 4):
        for i in starshipsjsons[x]['results']:
            # print(i)
            starships_names.append(i['name'])
            starships_url.append(i['url'])
    # pprint(starships_url)

    for i in starships_url:
        starships_info.append(requests.get(i).json())
    # pprint(starships_info)

    for i in starships_info:
        pilot_urls_with_empties.append(i.get('result').get('properties').get('pilots'))
    # pprint(pilot_urls)
    pilot_url_without_empties = [x for x in pilot_urls_with_empties if x]
    # pprint(pilot_url_without_empties)

    for lists in pilot_url_without_empties:
        for elements in lists:
            pilot_info.append(requests.get(elements).json())

    for i in pilot_url_without_empties:
        for x in i:
            pilot_urls_ind.append(x)
    # pprint(pilot_urls_ind)

    for i in pilot_info:
        pilot_names.append(i.get('result').get('properties').get('name'))
    # pprint(pilot_names)


def making_pilot_collection():
    collecting_starships_and_pilots()
    db.create_collection("pilots")
    for i in pilot_names:
        db.pilots.insert_one({
            "name": i,
            "pilot_id": db.characters.find_one({"name": i}, {"_id": 1}) })

    joined = db.pilots.aggregate([{
        "$lookup": {
            "from": "characters",
            "localField": "name._id",
            "foreignField": "_id",
             "as": "matched_name"
        }
    }])
    # for x in joined:
    #     print(x)


def making_dictionary():
    making_pilot_collection()
    matching_ids = []
    for i in pilot_names:
        matching_ids.append(db.pilots.find_one({"name": i}, {"_id":0, "pilot_id._id": 1}))
    # pprint(matching_ids)

    pilot_matchingid_dict = dict(zip(pilot_urls_ind,matching_ids))
    pprint(pilot_matchingid_dict)


making_dictionary()

