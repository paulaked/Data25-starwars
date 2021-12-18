# Assembly file

import requests
import json
from pprint import pprint
from app import func_page
from tests import testing

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
for i in pilot_urls_flat:
    people_info = func_page.api_request(i)
    pilot_id = people_info["result"]["_id"]
    pilot_id_list.append(pilot_id)
#pprint(pilot_id_list)

# Code to create a dictionary of people url and pilot_id
key_list = pilot_urls_flat
value_list = pilot_id_list
people_url_id = {k: v for k,v in zip(key_list,value_list)}
#print(people_url_id)

for url in url_list_ship:
    ship_data = func_page.api_request(url)
    list_url = []
    for p_url in ship_data["result"]["properties"]["pilots"]:
        list_url.append(p_url)
    for i in list_url:
        if list_url in people_url_id.keys():
            ship_data["result"]["properties"]["pilots"] = people_url_id[list_url]
    print(ship_data)
    #     if p_url in people_url_id.keys():
    #         ship_data["result"]["properties"]["pilots"] = people_url_id[p_url]
    # print(ship_data)


# for url in url_list_ship:
#     ship_data = func_page.api_request(url)
#     for p_url in ship_data["result"]["properties"]["pilots"]:
#         print(len(p_url))
#         if p_url in people_url_id.keys():
#             ship_data["result"]["properties"]["pilots"] = people_url_id[p_url]
#     print(ship_data)


# Pilot id is the url for the person who pilots the ship
# we want to replace the pilot ID with the _id from each person dictionary
# we want to make a dictionary {["people ID]:["_Id]}
# then can use panda to replace the information in each starship dictionary to show the pilot IDs instead of URLs

# Extract _id for each pilot URL, then make a dictionary where key is the URL and value IS id
















######### Testing
# An area to test the functions are working correctly, further comments in testing.py
# testing.func_one_test(web_address)
#
# testing.func_two_test(page_url, page_contents)
