# Assembly file

import requests
import json

from app import func_page

api_address = "https://www.swapi.tech/api/starships"


web_address = api_address
page_url = []
while True:
    page_contents = func_page.api_request(web_address)
    nextpage_url = func_page.turn_page(page_contents)
    if nextpage_url == None:
        break
    page_url.append(nextpage_url)
    web_address = nextpage_url
print(page_url)

for url in page_url:
