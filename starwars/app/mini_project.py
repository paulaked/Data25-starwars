# 1. Import necessary python libraries:
import requests
import pymongo
import json
from pprint import pprint

# 2. Connecting and using Starwars database on Mongocb:
client = pymongo.MongoClient()
db = client['starwars']

# starship API address:
web_address = 'https://www.swapi.tech/api/starships'


# 3. The following function extract the data from the corresponding API address:
def extract_data(url):
    starship_url = requests.get(url)
    starship_url = starship_url.json()
    return starship_url

# 4. The urls for the first page is stored as a list:
starship_page = [value['url'] for value in extract_data(web_address)['results']]


# 5. The following function extract the starship's urls for pages 2,3 and 4 and add them to the previous list:
def get_url_for_all_pages():
    current_page = extract_data(web_address)
    while current_page['next'] != None:
        current_page = requests.get(current_page['next'])
        current_page = current_page.json()
        for item in current_page['results']:
            starship_page.append(item['url'])
    return starship_page


# 6. The last function extracts the name of the pilots and find the their id on character collection and replace
# the pilot values with the matching ids:
def get_and_replace_pilots_id():
    starships = []
    for i in get_url_for_all_pages():
        url_content = requests.get(i)
        url_content = url_content.json()
        result = url_content['result']
        properties = result['properties']
        pilot_url = properties['pilots']
        pilot_name = []
        for pilot in pilot_url:
            pilot_content = requests.get(pilot)
            pilot_content = pilot_content.json()
            pilot_name.append(pilot_content['result']['properties']['name'])
        pilots_id = []
        for i in pilot_name:
            for n in db.characters.find({'name': i}):
                pilots_id.append(n["_id"])
        url_content['result']['properties']['pilots'] = pilots_id

        starships.append(url_content)

    return starships


# 7. Drop the existing starship collection from Mongodb:
db.drop_collection("Starship")
print('dropped')

# 8. Creating the starship collecton if it doesn't exist on Mongodb:
db.create_collection("Starship")
print('the collection was created successfully')

# 9. Different starships are added to the Starship collection on Mongodb:
for i in get_and_replace_pilots_id():
    db.Starship.insert_one(i)


print("all the available starship are added successfully")



