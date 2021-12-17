#  imports
import json
import pymongo
import requests
from pprint import pprint
from app import function_list
#
api_address = 'https://www.swapi.tech/api/starships'

web_address = api_address
next_page_url_list = [api_address]
while True:
    page_contents = function_list.extract_data(web_address)
    next_page_url = function_list.get_all_page_urls(page_contents)
    if next_page_url ==None:
        break
    next_page_url_list.append(next_page_url)
    web_address = next_page_url

print(next_page_url_list)
for url in next_page_url_list:
    data = function_list.extract_data(url)
    for i in data['results']:
        pprint(i['url'])

api_address_people = 'https://www.swapi.tech/api/people'

web_address_people = api_address_people
next_page_url_list_people = [api_address_people]
while True:
    page_contents_people = function_list.extract_data(web_address_people)
    next_page_url_people = function_list.get_all_page_urls(page_contents_people)
    if next_page_url_people == None:
        break
    next_page_url_list_people.append(next_page_url_people)
    web_address_people = next_page_url_people
print(next_page_url_list_people)
for url in next_page_url_list_people:
    data = function_list.extract_data(url)
    for i in data['results']:
        pprint(i['url'])

