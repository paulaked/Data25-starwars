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

#  ________________________________________________________  #

# Write code to extract the pilot URLs from each starship

list_of_pilot_urls = []
for url in list_of_starships:
    starship_info = function_list.extract_data(url)
    pilot_url = starship_info['result']['properties']['pilots']
    list_of_pilot_urls.append(pilot_url)
list_of_pilot_urls = [x for x in list_of_pilot_urls if x]
#print(list_of_pilot_urls)

#  ________________________________________________________  #


# Write code to extract each pilot's Object ID from the pilot URLs
pilot_urls_flat = []                    # multiply out the brackets! well not really. just erase the brackets
for sublist in list_of_pilot_urls:
    for item in sublist:
        pilot_urls_flat.append(item)
#get the IDs!
pilot_id_list = []
for url in pilot_urls_flat:
    people_info = function_list.extract_data(url)
    pilot_id = people_info['result']['_id']
    pilot_id_list.append(pilot_id)


key_list = pilot_urls_flat
value_list = pilot_id_list
zip_iterator = zip(key_list, value_list)
dictionary_of_pilot_ids = dict(zip_iterator)
pprint(dictionary_of_pilot_ids)


# pilot id is the url for the person who pilots the ship
# we want to replace the pilot ID with the _id from each person dictionary
# we want to make a dictionary of {['pilot ID']:['_id']}
# Use panda replace to change the information in each starship dictionary to show the pilot IDs instead of URLs.
#  ________________________________________________________  #
# extract an id for each pilot URL, then make dictionary where key is URL and value is ID
