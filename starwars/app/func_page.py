# Creating functions to use APIs

import requests


# Create a function to use an API to retrieve data
def api_request(url):
    raw_data = requests.get(url)
    json_data = raw_data.json()
    return json_data


# Create a function t take in current page of data and returns url of next page
def turn_page(json_data):
    if json_data["next"] != "null":
        next_page_url = json_data["next"]
        return next_page_url
    else:
        return False


# Create a function to make a dictionary
# def make_dict(key, value):
#     new_dict = {k: v for k, v in zip(key, value)}
#     return new_dict


# Create a function to make a list of the starship urls - specific function to this task
# def url_in_api(page_url_info):
#     url_list_ship = []  # A list of all starship url
#     for url in page_url_info:
#         data = api_request(url)
#         for i in data["results"]:
#             url_list_ship.append(i["url"])
#     return url_list_ship
#
#
# def pilot_url_list(url_list_ship_info):
#     ship_pilot_url = []
#     for i in url_list_ship_info:
#         ship_info = api_request(i)
#         pilot_url = ship_info["result"]["properties"]["pilots"]
#         ship_pilot_url.append(pilot_url)
#     return ship_pilot_url
