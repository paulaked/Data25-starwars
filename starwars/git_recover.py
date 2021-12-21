import requests
import json
import pymongo
from pprint import pprint
from app import func_page
from tests import testing
##code to import information to mongodb
client = pymongo.MongoClient()
db = client["starwars"]
db.drop_collection("starships")  #Drops collection if exists
db.create_collection("starships")

# Code to access the starship information
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
#print(page_url)
# An empty list to append the url link on the individual starships
url_list_ship = []  # A list of all starship url
for url in page_url:
    data = func_page.api_request(url)
    for i in data["results"]:
        url_list_ship.append(i["url"])
#pprint(url_list_ship)
#print(len(url_list_ship))
############################################################# Code to access the people information
# api_address_people = "https://www.swapi.tech/api/people"
# web_address = api_address_people
#
# # Code to append the remaining urls of the pages
# page_people_url = [api_address_people]
# while True:
#     page_contents_people = func_page.api_request(web_address)
#     nextpage_url = func_page.turn_page(page_contents_people)
#     if nextpage_url == None:
#         break
#     page_people_url.append(nextpage_url)
#     web_address = nextpage_url
#print(page_people_url)
# code to append the urls of the individual pilots to the empty list url_list_people
# url_list_people = []
# for url in page_people_url:
#     data = func_page.api_request(url)
#     for i in data["results"]:
#         url_list_people.append(i["url"])
#pprint(url_list_people)
# Code to access just the pilot url and and append them to an empty list. return only values that arent empty
ship_pilot_url = []
for i in url_list_ship:
    ship_info = func_page.api_request(i)
    pilot_url = ship_info["result"]["properties"]["pilots"]
    ship_pilot_url.append(pilot_url)
ship_pilot_url = [x for x in ship_pilot_url if x]
#pprint(ship_pilot_url)
#Code to flatten the list of urls to remove a list of lists
pilot_urls_flat = []
for sublist in ship_pilot_url:
    for item in sublist:
        pilot_urls_flat.append(item)
#pprint(pilot_urls_flat)

#Code to access the pilot_id from each url
pilot_id_list = []
#Code to access the name from each url
pilot_name_list = []
for i in pilot_urls_flat:
    people_info = func_page.api_request(i)
    pilot_id = people_info["result"]["_id"]
    pilot_id_list.append(pilot_id)
#pprint(pilot_id_list)
    pilot_id = people_info["result"]["properties"]["name"]
    pilot_name_list.append(pilot_id)
#pprint(pilot_name_list)

#Code to access the character id after matching names with api and mongo database
mongo_name_id_list = []
for name in pilot_name_list:
     mongo_name_id = db.characters.find_one({"name":name},{"_id":1})
     mongo_name_id_list.append(mongo_name_id)
#print(mongo_name_id_list)


# Code to create a dictionary of people url and pilot_id
key_list = pilot_urls_flat
value_list = pilot_id_list
people_url_id = {k: v for k,v in zip(key_list,value_list)}
#print(people_url_id)
value_list = mongo_name_id_list
pilurl_mongoname_id = {k: v for k,v in zip(key_list,value_list)}
#print(pilurl_mongoname_id)

#code ti make ship data equal a list of person objectid, and placed in a created database called starships
for url in url_list_ship:
    ship_data = func_page.api_request(url)
    people_url_id_list = []
    for p_url in ship_data["result"]["properties"]["pilots"]:
        if p_url == []:
            pass
        else:
            people_url_id_list.append(people_url_id[p_url])
            people_url_id_list.append(pilurl_mongoname_id[p_url])
            ship_data["result"]["properties"]["pilots"] = people_url_id_list
    db.starships.insert_one(ship_data)