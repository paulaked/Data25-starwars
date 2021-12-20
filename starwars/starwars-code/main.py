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


def collecting_starships_and_pilots():
    starships_names = []
    starships_url = []
    for x in range(0, 4):
        for i in starshipsjsons[x]['results']:
            # print(i)
            starships_names.append(i['name'])
            starships_url.append(i['url'])
    # pprint(starships_url)

    starships_info = []
    for i in starships_url:
        starships_info.append(requests.get(i).json())
    # pprint(starships_info)

    pilot_urls = []
    for i in starships_info:
        pilot_urls.append(i.get('result').get('properties').get('pilots'))
    # pprint(pilot_urls)
    pilot_url2 = [x for x in pilot_urls if x]
    # pprint(pilot_url2)
    pilot_info = []
    pilot_names = []
    for lists in pilot_url2:
        for elements in lists:
            pilot_info.append(requests.get(elements).json())

    for i in pilot_info:
        pilot_names.append(i.get('result').get('properties').get('name'))
    pprint(pilot_names)

    db.create_collection("pilots")
    for i in pilot_names:
        db.pilots.insert_one({
            "name": i,
            "pilot_id": db.characters.find_one({"name": i}, {"_id": 1}) })




collecting_starships_and_pilots()

