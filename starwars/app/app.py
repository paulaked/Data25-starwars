import requests


class ApiRequest:

    def __init__(self, api_address):
        self.api_address = api_address


    def get_request(self):
        response = requests.get(self.api_address)
        return response

    def make_json(self, response):
        self.response = response
        response_json = response.json()
        return response_json


class StarshipUrls(ApiRequest):
    def __init__(self, response_json):
        response_json.self = response_json
        super().__init__(self)


    def collect_urls(self):
        data = super().make_json(super().response)
        starship_urls = []
        for page in range(1, data["total_pages"] + 1):
            address = super().api_address + "?page=" + str(page) + "&limit=10"
            starships = super(address).get_request()
            starships = super().make_json(starships)
            for dict in starships["results"]:
                starship_urls.append(dict["url"])
        return starship_urls

# class CollectPilotNames(StarshipUrls):
#     def __init__(self, starship_urls):
#         CollectPilotNames.__init__(self, starship_urls)
#
