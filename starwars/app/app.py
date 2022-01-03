import requests
import pymongo

client = pymongo.MongoClient()
db = client["starwars"]


def get_request(api_address):
    api_response = requests.get(api_address)
    return api_response


def make_json(api_response):
    response_json = api_response.json()
    return response_json


def collect_urls(api_address, response_json):
    starship_urls = []
    for page in range(1, response_json["total_pages"] + 1):
        starships_page_address = api_address + "?page=" + str(page) + "&limit=10"
        starships_page_content = make_json(get_request(starships_page_address))
        for dict in starships_page_content["results"]:
            starship_urls.append(dict["url"])
    return starship_urls


def collect_pilot_urls(starship_urls):
    pilot_urls_list = []
    for url in starship_urls:
        starships_page_content = make_json(get_request(url))
        pilot_urls_list.append(starships_page_content["result"]["properties"]["pilots"])
    return pilot_urls_list


def only_urls(pilot_urls_list):
    pilot_urls_lists = [url for url in pilot_urls_list if url]
    pilot_urls = []
    for sublist in pilot_urls_lists:
        for url in sublist:
            pilot_urls.append(url)
    return pilot_urls


def collect_pilot_names(pilot_urls):
    pilot_names = []
    for url in pilot_urls:
        pilot_data = make_json(get_request(url))
        pilot_names.append(pilot_data["result"]["properties"]["name"])
    return pilot_names


def collect_object_ids(pilot_names):
    obj_ids = []
    for name in pilot_names:
        obj_id = db.characters.find_one({"name": name}, {"_id": 1})
        obj_ids.append(obj_id)
    return obj_ids


def create_dictionary(pilot_urls, obj_ids):
    pilot_urls_obj_ids_dict = {}
    for i in range(len(pilot_urls)):
        pilot_urls_obj_ids_dict[pilot_urls[i]] = obj_ids[i]
    return pilot_urls_obj_ids_dict


def create_collection(name):
    db.drop_collection(name)
    db.create_collection(name)


def swap_urls_for_ids(starship_urls, dict):
    for url in starship_urls:
        data = make_json(get_request(url))
        pilot_obj_ids_at_pilot_location = []
        for pilot_url in data["result"]["properties"]["pilots"]:
            if pilot_url==[]:
                pass
            else:
                pilot_obj_ids_at_pilot_location.append(dict[pilot_url])
                data["result"]["properties"]["pilots"] = pilot_obj_ids_at_pilot_location
        db.starships.insert_one(data)
