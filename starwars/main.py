# Main file for final code
import pymongo
from pprint import pprint
from app import func_page

client = pymongo.MongoClient()
db = client["starwars"]

api_address_ship = "https://www.swapi.tech/api/starships"
web_address = api_address_ship
page_url = [api_address_ship]

# Code to access the 3 remaining urls of the pages and appended to page_url list
while True:
    page_contents = func_page.api_request(web_address)
    nextpage_url = func_page.turn_page(page_contents)
    if nextpage_url == None:
        break
    page_url.append(nextpage_url)
    web_address = nextpage_url

url_list_ship = []  # A list of all starship url
for url in page_url:
    data = func_page.api_request(url)
    for i in data["results"]:
        url_list_ship.append(i["url"])

ship_pilot_url = []
for i in url_list_ship:
    ship_info = func_page.api_request(i)
    pilot_url = ship_info["result"]["properties"]["pilots"]
    ship_pilot_url.append(pilot_url)
ship_pilot_url = [x for x in ship_pilot_url if x]
#print(ship_pilot_url)

pilot_urls_flat = []
for sublist in ship_pilot_url:
    for item in sublist:
        pilot_urls_flat.append(item)

pilot_id_list = []
for i in pilot_urls_flat:
    people_info = func_page.api_request(i)
    pilot_id = people_info["result"]["_id"]       #["name"]["properties"]["name"]
    pilot_id_list.append(pilot_id)
pprint(pilot_id_list)

# for i in name:
#     mongo_name_id = db.characters.find_one({"name":i},{"_id":1})
#     print(mongo_name_id)