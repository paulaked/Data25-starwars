#  Imports

import json
import pymongo
import requests

#  Create a function utilising API to retrieve data


def extract_data(url):
    raw_data = requests.get(url)
    json_data = raw_data.json()
    return json_data


#  Create function to cycle through all pages

def extract_all_pages(json_data):
    url_list = []
    for result in json_data["results"]:
        url_list.append(result["url"])
    if json_data["next"] != 'null':
        url_list.append(extract_data(json_data["next"]))
    return url_list

'''
    if json_data_starships["next"] != null:
        page_n = requests.get(json_data_starships["next"])
'''