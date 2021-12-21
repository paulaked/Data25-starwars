import requests


class GetAllStarshipUrls:

    def __init__(self, api_address):
        self.api_address = api_address


    def get_request(self):
        page_content = requests.get(self.api_address).json()
        return page_content

        # Function that requests an address and returns
        # the response as a .json format.
    def collect_urls

    def next_page