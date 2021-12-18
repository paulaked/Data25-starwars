# Creating functions to use APIs

import requests
import json

# Create a function to use an API to retrieve data
def api_request(url):
    raw_data = requests.get(url)
    json_data = raw_data.json()
    return(json_data)

# Create a function t take in current page of data and returns url of next page
def turn_page(json_data):
    if json_data["next"] != "null":
        next_page_url = json_data["next"]
        return next_page_url
    else:
        return False
# Create a function to extract information from all pages


# def extract_url(json_data):
#     starship_url = []
#     for i in json_data["results"]:
#         starship_url.append(i["url"])
#         print(i["url"])
#     if json_data["next"] != "null":
#         raw_next_page = requests.get(json_data["next"])
#         json_next_page = raw_next_page.json()
#         for i in json_next_page["results"]:
#             print(i["url"])
# #    return starship_url

#One to first access the page
# One to extract
# One to go to next page