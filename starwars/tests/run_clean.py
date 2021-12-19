#  Import modules for script to run
import pymongo
from app import function_list

#  Specify client to utilise MongoDB
#  Create collection
#  Specify api address
client = pymongo.MongoClient()
db = client['starwars']
db.create_collection('starshipswids')
api_address = 'https://www.swapi.tech/api/starships'

#  Remember to drop any formerly used starship databases within MongoDB Compass

#  Make a list of all page URLs that the API holds
web_address = api_address
next_page_url_list = [api_address]
while True:
    page_contents = function_list.extract_data(web_address)
    next_page_url = function_list.get_all_page_urls(page_contents)
    if next_page_url == None:
        break
    next_page_url_list.append(next_page_url)
    web_address = next_page_url

#  Create a list of each starship
list_of_starships = []
for url in next_page_url_list:
    data = function_list.extract_data(url)
    for i in data['results']:
        list_of_starships.append(i['url'])


#  Create a list of the pilot URLs
list_of_pilot_urls = []
for url in list_of_starships:
    starship_info = function_list.extract_data(url)
    pilot_url = starship_info['result']['properties']['pilots']
    list_of_pilot_urls.append(pilot_url)
list_of_pilot_urls = [x for x in list_of_pilot_urls if x]

#  The list of pilot URLs is a list of lists
#  Create a list of individual elements (URLs of each pilot)
pilot_urls_flat = []
for sublist in list_of_pilot_urls:
    for item in sublist:
        pilot_urls_flat.append(item)

#  Create list of IDs associated with each pilot
pilot_id_list = []
for url in pilot_urls_flat:
    people_info = function_list.extract_data(url)
    pilot_id = people_info['result']['_id']
    pilot_id_list.append(pilot_id)

#  Create dictionary, matching URL to ID
new_dict = {k: v for k, v in zip(pilot_urls_flat,pilot_id_list)}

#  Replace each pilot URL in each starship entry with the pilot's ID
#  Insert all entries to the new database
for url in list_of_starships:
    ship_info = function_list.extract_data(url)
    pilot_id_list_again = []
    for i in ship_info['result']['properties']['pilots']:
        if i == []:
            pass
        else:
            pilot_id_list_again.append(new_dict[i])
            ship_info['result']['properties']['pilots'] = pilot_id_list_again
    db.starshipswids.insert_one(ship_info)

