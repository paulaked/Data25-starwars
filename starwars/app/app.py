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
        starships_page_content = get_request(starships_page_address)
        starships_page_content = make_json(starships_page_content)
        for dict in starships_page_content["results"]:
            starship_urls.append(dict["url"])
    return starship_urls

