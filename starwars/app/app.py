import requests


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
    pilot_urls = []
    for url in starship_urls:
        starships_page_content = make_json(get_request(url))
        pilot_urls.append(starships_page_content["result"]["properties"]["pilots"])
    return pilot_urls

def collect_pilot_names(pilot_urls):
    pilot_names = []
    for list_of_urls in pilot_urls:
        for url in list_of_urls
            pilot_data = make_json(get_request(url))
            pilot_names.append(pilot_data["result"]["properties"]["name"])
    return pilot_names
