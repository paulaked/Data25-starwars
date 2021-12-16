import pymongo
from pprint import pprint
import json
import requests
'''
plan
extract starship data
write function to read and extract dictionaries about people within the startship
output the starship data with pilots being people ID
may not have to dump to a file
'''
raw_data_people = requests.get('https://www.swapi.tech/api/people')
#pprint(raw_data_people.json())

raw_data_starships = requests.get('https://www.swapi.tech/api/starships')
pprint(raw_data_starships) # when .json() that gives output I want
#  create new variable to dump the request output in json format
json_data_starships = raw_data_starships.json()
pprint(json_data_starships)


#dictionary = {"starship":"tatooine"}
with open("starships_API_with_URLs","w") as jsonfile:
    json.dump(json_data_starships, jsonfile)


#
# response = requests.get('https://www.swapi.tech/api/starships')
# print(response.status_code)
# ship = response.json()
# #pprint(ship)
# for val in ship['results':'url']:
#     print(val)