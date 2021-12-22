import pymongo
import requests

client = pymongo.MongoClient()
db = client["starwars"]
db.drop_collection("starships")
db.create_collection("starships")

contents = requests.get("https://www.swapi.tech/api/starships")
ship = contents.json()
#print(ship)
my_list = []
for val in ship['results']:
    my_list.append(val["url"])
#print(my_list)

if ship['next'] != None:
    next_page = requests.get(ship['next'])
    page_two = next_page.json()
    for i in page_two['results']:
        my_list.append(i['url'])
    if page_two['next'] != None:
        next_page = requests.get(page_two['next'])
        page_three = next_page.json()
        for ul in page_three['results']:
            my_list.append(ul['url'])
        if page_three['next'] != None:
            next_page = requests.get(page_three['next'])
            page_four = next_page.json()
            for n in page_four['results']:
                my_list.append(n['url'])
# print(my_list)

ship_pilot_url = []
for i in my_list:
    content = requests.get(i)
    info = content.json()
    pilot_url = info["result"]["properties"]["pilots"]
    ship_pilot_url.append(pilot_url)
# print(ship_pilot_url)
ship_pilot_url = [x for x in ship_pilot_url if x]
# print(ship_pilot_url)

pilot_url_flat = []
for sublist in ship_pilot_url:
    for i in sublist:
        pilot_url_flat.append(i)
#print(pilot_url_flat)

pilot_name_list = []
for url in pilot_url_flat:
    content = requests.get(url)
    pilot_json = content.json()
    pilot_name = pilot_json["result"]["properties"]["name"]
    pilot_name_list.append(pilot_name)
#print(pilot_name_list)

mongo_name_id_list = []
for name in pilot_name_list:
    mongo_name_id = db.characters.find_one({"name": name}, {"_id": 1})
    mongo_name_id_list.append(mongo_name_id)

pilot_url_mongo_id = {k: v for k, v in zip(pilot_url_flat, mongo_name_id_list)}
#print(pilot_url_mongo_id)

for url in my_list:
    people_url_id_list = []
    content = requests.get(url)
    ship_info = content.json()
    for i in ship_info["result"]["properties"]["pilots"]:
        if i == []:
            pass
        else:
            people_url_id_list.append(pilot_url_mongo_id[i])
            ship_info["result"]["properties"]["pilots"] = people_url_id_list
    db.starships.insert_one(ship_info)

# This code works when no functions are used. Previous runs worked but proved to be fragile.
# Previous runs wouldn't work or upload more than 26/36 results.
# Additionally, previous runs were tested on other machines and worked.
# Due to this, limited testing has been achieved, naturally no functions have been included.
# A different run will be wrote with functions but wont upload to pymongo.