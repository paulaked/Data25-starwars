# Assembly file

import requests
import json
from pprint import pprint
from app import func_page
from tests import testing

api_address = "https://www.swapi.tech/api/starships"
web_address = api_address
page_url = [api_address]

while True:
    page_contents = func_page.api_request(web_address)
    nextpage_url = func_page.turn_page(page_contents)
    if nextpage_url == None:
        break
    page_url.append(nextpage_url)
    web_address = nextpage_url
#print(page_url)

url_list = []
for url in page_url:
    data = func_page.api_request(url)
    for i in data["results"]:
        url_list.append(i["url"])
#pprint(url_list)


######### Testing

testing.func_one_test(web_address)

testing.func_two_test(page_url, page_contents)
