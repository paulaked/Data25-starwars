# Assembly file

import requests
import json
from pprint import pprint
from app import func_page
from tests import testing

api_address_ship = "https://www.swapi.tech/api/starships"
web_address = api_address_ship
page_url = [api_address_ship]

while True:
    page_contents = func_page.api_request(web_address)
    nextpage_url = func_page.turn_page(page_contents)
    if nextpage_url == None:
        break
    page_url.append(nextpage_url)
    web_address = nextpage_url
#print(page_url)

url_list_ship = []
for url in page_url:
    data = func_page.api_request(url)
    for i in data["results"]:
        url_list_ship.append(i["url"])
#pprint(url_list_ship)

api_address_people = "https://www.swapi.tech/api/people"
web_address = api_address_people

page_people_url = [api_address_people]
while True:
    page_contents_people = func_page.api_request(web_address)
    nextpage_url = func_page.turn_page(page_contents_people)
    if nextpage_url == None:
        break
    page_people_url.append(nextpage_url)
    web_address = nextpage_url
#print(page_people_url)

url_list_people = []
for url in page_people_url:
    data = func_page.api_request(url)
    for i in data["results"]:
        url_list_people.append(i["url"])
pprint(url_list_people)






######### Testing

# testing.func_one_test(web_address)
#
# testing.func_two_test(page_url, page_contents)
