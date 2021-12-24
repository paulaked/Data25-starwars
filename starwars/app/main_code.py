import requests
import json
from pprint import pprint
import os
import pymongo

# Retrieve starwars api data from swapi
# Convert api to json format
# Starship info spread across 4 pages
# response1 = requests.get('https://swapi.dev/api/starships/').json()
# response2 = requests.get(response1['next']).json()
# response3 = requests.get(response2['next']).json()
# response4 = requests.get(response3['next']).json()


# Collect only starship info from each page into a list
# def collect_results():
#     starship_id = []
#     for i in response1['results']:
#         starship_id.append(i)
#
#     for i in response2['results']:
#         starship_id.append(i)
#
#     for i in response3['results']:
#         starship_id.append(i)
#
#     for i in response4['results']:
#         starship_id.append(i)
#     return starship_id
#
# # pprint(collect_results())
#
#
# # Collect all starship urls into a list
# def collect_urls():
#     starship_urls =[]
#     for i in collect_results():
#         starship_urls.append(i['url'])
#     return starship_urls
#
# # pprint(collect_urls())
#
# # Change pilot urls from the starship list to pilot name
# def change_pilot_urls_to_name():
#     starships_updated =[]
#     for i in collect_results():
#         pilot_names = []
#         for j in i['pilots']:
#             pilot_names.append(requests.get(j).json()['name'])
#         i.update({'pilots': pilot_names})
#         starships_updated.append(i)
#     return  starships_updated

# pprint(change_pilot_urls_to_name())


client = pymongo.MongoClient()
db = client['star_wars_3']
sw_starships = db['starship_info']
sw_characters = db['character_info']

# Create directory in locally/repository manually
# for i in change_pilot_urls_to_name():
#     with open(os.path.join('starships', i['name'] + '.json'), 'w') as f:
#         f.write(json.dumps(i))

# Upload starship collection to mongoDB
# for i in os.listdir('starships'):
#     with open(os.path.join('starships', i), 'r') as f:
#         # print(f.read())
#         up = sw_starships.insert_one(json.load(f))

for i in sw_starships.find():
    pilots = []
    for j in i['pilots']:
        unique_character_id = sw_characters.find_one({'name': j})['_id']
        match_id = {'_id': unique_character_id}
        pilots.append(match_id)
    sw_starships.update_one({'name': i['name']}, {'$set': {'pilots': pilots}})




# pprint(response1)
# pprint(response2)
# pprint(response3)
# pprint(response4)