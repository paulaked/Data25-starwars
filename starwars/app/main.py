import requests
import pymongo
import json
from pprint import pprint




response = requests.get('https://www.swapi.tech/api/starships')
#print(response.status_code)
ship = response.json()
#pprint(ship)
my_list = []
for val in ship['results']:
    for value in val.values():
        my_list.append(value)

url_list = []
for i in my_list:
    if i[0] == 'h':
        url_list.append(i)

if ship['next'] != None:
    next_page = requests.get(ship['next'])
    page_two = next_page.json()
    for item in page_two['results']:
        url_list.append(item['url'])
    if page_two['next'] != None:
        next_page3 = requests.get(page_two['next'])
        page_three = next_page3.json()
        for ul in page_three['results']:
            url_list.append(ul['url'])
        if page_three['next'] != None:
            next_page4 = requests.get(page_three['next'])
            page_four = next_page4.json()
            for n in page_four['results']:
                url_list.append(n['url'])


pprint(url_list)
#print(len(url_list))
#for i in url_list:
    #print(i)
client = pymongo.MongoClient() # putting nothing here means the database is local
db = client['starwars']


starships = []
for i in url_list:
    url_content = requests.get(i)
    url_content = url_content.json()
    # print(url_content)
    result = url_content['result']
    properties = result['properties']
    pilot_url = properties['pilots']
    # if pilot_url == []:
    #     continue

    pilot_name = []
    for pilot in pilot_url:

        pilot_content = requests.get(pilot)
        pilot_content = pilot_content.json()
        pilot_name.append(pilot_content['result']['properties']['name'])

    pilots_id = []
    for i in pilot_name:
        for n in db.characters.find({'name': i}):
            pilots_id.append(n["_id"])
    url_content['result']['properties']['pilots'] = pilots_id




    starships.append(url_content)


# for i in starships:
#     db.Starship.insert_one(i)




print("done")













#print(len(url_list))
#print(url_list)







