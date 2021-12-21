import pymongo
from app import func_page
from pprint import pprint

client = pymongo.MongoClient()
db = client["starwars"]
db.drop_collection("starships")
db.create_collection("starships")

api_address = "https://www.swapi.tech/api/starships"
web_address = api_address
page_url = [api_address]

while True:
    page_content = func_page.api_request(web_address)
    next_page = func_page.turn_page(page_content)
    if next_page == None:
        break
    page_url.append(next_page)      # Maybe else
    web_address = next_page

url_list_ship = []
for url in page_url:
    info = func_page.api_request(url)
    for i in info["results"]:
        url_list_ship.append(i["url"])

ship_pilot_url = []
for i in url_list_ship:
    ship_info = func_page.api_request(i)
    pilot_url = ship_info["result"]["properties"]["pilots"]
    ship_pilot_url.append(pilot_url)

ship_pilot_url = [x for x in ship_pilot_url if x]

pilot_urls_flat = []
for sublist in ship_pilot_url:
    for i in sublist:
        pilot_urls_flat.append(i)

pilot_name_list = []
for url in pilot_urls_flat:
    pilot_info = func_page.api_request(url)
    pilot_name = pilot_info["result"]["properties"]["name"]
    pilot_name_list.append(pilot_name)

mongo_name_id_list = []
for name in pilot_name_list:
    mongo_name_id = db.characters.find_one({"name": name}, {"_id": 1})
    mongo_name_id_list.append(mongo_name_id)

pilot_url_mongo_id = {k: v for k, v in zip(pilot_urls_flat, mongo_name_id_list)}

for url in url_list_ship:
    ship_info = func_page.api_request(url)
    people_url_id_list = []
    for i in ship_info["result"]["properties"]["pilots"]:
        if i == []:
            pass
        else:
            people_url_id_list.append(pilot_url_mongo_id[i])
            ship_info["result"]["properties"]["pilots"] = people_url_id_list
    db.starships.insert_one(ship_info)
