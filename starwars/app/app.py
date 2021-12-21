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
        return self.response.json()

        # Function that requests an address and returns
        # the response as a .json format.

    # def collect_urls(self, page_content):
    #     self.page_content = page_content
    #     url_list = []
    #     for result in page_content["results"]:
    #         url_list.append(result["url"])
    #     return url_list
    #
    #     # Function that returns a list of starship urls
    #     # from the  api page
