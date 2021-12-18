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
    if next_page_url == None:
        break
    next_page_url_list.append(next_page_url)
    web_address = next_page_url

#print(next_page_url_list)
list_of_starships = []
for url in next_page_url_list:
    data = function_list.extract_data(url)
    for i in data['results']:
        list_of_starships.append(i['url'])
#        pprint(i['url'])
#pprint(list_of_starships)
#  ________________________________________________________  #


api_address_people = 'https://www.swapi.tech/api/people'  # Inputting address for API to target
web_address_people = api_address_people
next_page_url_list_people = [api_address_people]          # Initialising list of URLs
while True:
    page_contents_people = function_list.extract_data(web_address_people)           # Extracting data on people
    next_page_url_people = function_list.get_all_page_urls(page_contents_people)    # Finding out whether on last page
    if next_page_url_people == None:
        break
    next_page_url_list_people.append(next_page_url_people)      # Adding url of next page to a list
    web_address_people = next_page_url_people                   # Moving on to the next page to check
#print(next_page_url_list_people)                                # Printing the list
list_of_people = []
for url in next_page_url_list_people:
    data = function_list.extract_data(url)
    for i in data['results']:
        list_of_people.append(i['url'])
#        pprint(i['url'])                                        # Print out the URL associated with each person
#pprint(list_of_people)
#  Write code to make dictionary of url and object(pilot) ID

#  ________________________________________________________  #

# Write code to extract the pilot ID from starship

list_of_pilot_urls = []
for url in list_of_starships:
    starship_info = function_list.extract_data(url)
    pilot_url = starship_info['result']['properties']['pilots']
    list_of_pilot_urls.append(pilot_url)
list_of_pilot_urls = [x for x in list_of_pilot_urls if x]
print(list_of_pilot_urls)

