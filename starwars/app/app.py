import requests


class StarshipUrls:

    def __init__(self):
        pass

    def get_request(self, api_address):
        self.api_address = api_address
        response = requests.get(self.api_address)
        return response

    def make_json(self, response):
        self.response = response
        response_json = self.response.json()
        return response_json

    def collect_urls(self, response_json, api_address):
        self.response_json = response_json
        self.api_address = api_address
        starship_urls = []
        for page in range(1, response_json["total_pages"] + 1):
            address = api_address + "?page=" + str(page) + "&limit=10"
            starships = StarshipUrls.get_request(StarshipUrls(), address)
            starships = StarshipUrls.make_json(StarshipUrls(), starships)
            for dict in starships["results"]:
                starship_urls.append(dict["url"])
        return starship_urls
