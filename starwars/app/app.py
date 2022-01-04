# app is a collection of functions used to requests data for each starship in the swappi api. The pilot urls for each
# starship are then swapped for corresponding object ids in the current characters collection locally stored as a
# mongodb database. The starship data is then added to a new starships collection in the same starwars database.

import requests
import pymongo

# configure the mongo db database
client = pymongo.MongoClient()
db = client["starwars"]


# get_request is a function that takes a web address as an input and returns the response from a get request.
def get_request(api_address):
    api_response = requests.get(api_address)
    return api_response


# make_json is a function that takes an api response as an input and outputs the response as a json format.
def make_json(api_response):
    response_json = api_response.json()
    return response_json


# collect_urls is a function that takes in the starships api address and the response to that address in a json
# format and outputs a list of all that starship page urls.
def collect_urls(api_address, response_json):
    starship_urls = []
    # the starship urls are spread over four pages, the total number of pages was iterated.
    for page in range(1, response_json["total_pages"] + 1):
        # to generate the url for the current starship page the api_address is modified with the current page number
        # within the range of total pages.
        starships_page_address = api_address + "?page=" + str(page) + "&limit=10"
        starships_page_content = make_json(get_request(starships_page_address))
        # content from each page is returned as nested dictionaries, the first layer of dictionaries is iterated
        # through and the starship urls extracted.
        for dict in starships_page_content["results"]:
            starship_urls.append(dict["url"])
    return starship_urls


# collect_pilot_urls takes the list of starship urls as an input and returns a list of web address where information
# about the pilot/s of each ship is located.
def collect_pilot_urls(starship_urls):
    pilot_urls_list = []
    for url in starship_urls:
        starships_page_content = make_json(get_request(url))
        pilot_urls_list.append(starships_page_content["result"]["properties"]["pilots"])
    return pilot_urls_list


# only_urls takes the pilot_urls_list as an input and returns a list of only the pilot urls. The pilots url list is a
# list made up of sub lists. Each sublist either contains none, single or multiple pilot urls. A single list of just
# pilot urls is required.
def only_urls(pilot_urls_list):
    # empty sub lists are filtered out of the pilot urls list.s.
    pilot_urls_lists = [url for url in pilot_urls_list if url]
    pilot_urls = []
    # a nested for loop firstly steps into each sublist then for each url appends that url to apilot urls.
    for sublist in pilot_urls_lists:
        for url in sublist:
            pilot_urls.append(url)
    return pilot_urls


# collect_pilot_names is a function which takes in a list of pilot urls and returns the character names stored at
# each pilot url.
def collect_pilot_names(pilot_urls):
    pilot_names = []
    for url in pilot_urls:
        pilot_data = make_json(get_request(url))
        pilot_names.append(pilot_data["result"]["properties"]["name"])
    return pilot_names


# collect_object_ids takes in a list of pilot names and returns the corespondings object ids stored in the current
# characters collection in the star wars database in mongodb.
def collect_object_ids(pilot_names):
    obj_ids = []
    for name in pilot_names:
        obj_id = db.characters.find_one({"name": name}, {"_id": 1})
        obj_ids.append(obj_id)
    return obj_ids


# create_dictionary takes in a list of keys and a list of values and returns a dictionary of key value pairs.
def create_dictionary(pilot_urls, obj_ids):
    pilot_urls_obj_ids_dict = {}
    for i in range(len(pilot_urls)):
        pilot_urls_obj_ids_dict[pilot_urls[i]] = obj_ids[i]
    return pilot_urls_obj_ids_dict


# create_collection is a function which takes name as an argument creates a new mongodb collection  with the same name.
def create_collection(name):
    db.drop_collection(name)
    db.create_collection(name)


# swap_urls_for_ids takes in spaceship_urls as a list and the dictionary of pilot names and object ids. The data at
# each starship url is requested. Whilst in RAM on the local machine the pilot url is swapped for the coresponding
# character object id. The updated starship data is then stored in the starships collection in the starwars mongodb
# database.
def swap_urls_for_ids(starship_urls, dict):
    # a request to each starship url is made
    for url in starship_urls:
        data = make_json(get_request(url))
        pilot_obj_ids_at_pilot_location = []
        # for each starship the pilot url is found and swapped with the coresponding object id using the pilot name
        # to match the two.
        for pilot_url in data["result"]["properties"]["pilots"]:
            if pilot_url==[]:
                pass
            else:
                pilot_obj_ids_at_pilot_location.append(dict[pilot_url])
                data["result"]["properties"]["pilots"] = pilot_obj_ids_at_pilot_location
        db.starships.insert_one(data)
