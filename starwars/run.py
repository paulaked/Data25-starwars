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
url_list_ship = []
for url in page_url:
    data = func_page.api_request(url)
    for i in data["results"]:
        url_list_ship.append(i["url"])
#pprint(url_list_ship)

ship_pilot_url = []
for i in url_list_ship:
    ship_info = func_page.api_request(i)
    pilot_url = ship_info["result"]["properties"]["pilots"]
    ship_pilot_url.append(pilot_url)
ship_pilot_url = [x for x in ship_pilot_url if x]
pprint(ship_pilot_url)


#     if ship_info["result"]["properties"]["pilots"] != []:
#         ship_pilot_url.append(ship_info)
#     else:
#         pass
# print(ship_pilot_url)
    #print(ship_info["result"]["properties"]["pilots"])









# Code to access the people information
api_address_people = "https://www.swapi.tech/api/people"
web_address = api_address_people

# Code to append the remaining urls of the pages
page_people_url = [api_address_people]
while True:
    page_contents_people = func_page.api_request(web_address)
    nextpage_url = func_page.turn_page(page_contents_people)
    if nextpage_url == None:
        break
    page_people_url.append(nextpage_url)
    web_address = nextpage_url
#print(page_people_url)

# code to append the urls of the individual pilots to the empty list url_list_people
url_list_people = []
for url in page_people_url:
    data = func_page.api_request(url)
    for i in data["results"]:
        url_list_people.append(i["url"])
#pprint(url_list_people)










######### Testing
# An area to test the functions are working correctly, further comments in testing.py
# testing.func_one_test(web_address)
#
# testing.func_two_test(page_url, page_contents)
