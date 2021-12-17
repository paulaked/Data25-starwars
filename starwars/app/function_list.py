#  Imports

import json
import pymongo
import requests

#  Create a function utilising API to retrieve data

def extract_data(url):
    raw_data = requests.get(url)
    json_data = raw_data.json()
    return json_data

#  Create a function to take in current page data, returning URL of next page
def get_all_page_urls(json_data):
    page_urls = []
    if json_data["next"] != 'null':
        get_all_page_urls = json_data["next"]
        return get_all_page_urls
    else:
        return False

#  visit all pages and extract data






#  Create function to cycle through all pages

def extract_all_pages(json_data):
    url_list = []
    for result in json_data["results"]:
        url_list.append(result["url"])
        if json_data["next"] != "null":
            raw_next_page = requests.get(json_data["next"])
            for i in raw_next_page['results']:
                print(i["url"])
            #print(next_page)

    if json_data["next"] != 'null':
        url_list.append(extract_data(json_data["next"]))
    return url_list

'''
    if json_data_starships["next"] != null:
        page_n = requests.get(json_data_starships["next"])
'''