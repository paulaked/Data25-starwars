import requests
import json
from pprint import pprint

# Retrieve starwars api data from swapi
# Convert api to json format
# Starship info spread across 4 pages
response1 = requests.get('https://swapi.dev/api/starships/').json()
response2 = requests.get(response1['next']).json()
response3 = requests.get(response2['next']).json()
response4 = requests.get(response3['next']).json()

# Collect only starship info from each page into a list
def collect_results():
    starship_id = []
    for i in response1['results']:
        starship_id.append(i)

    for i in response2['results']:
        starship_id.append(i)

    for i in response3['results']:
        starship_id.append(i)

    for i in response4['results']:
        starship_id.append(i)
    return starship_id

# pprint(collect_results())

# Collect all starship urls into a list
def collect_urls():
    starship_urls =[]
    for i in collect_results():
        starship_urls.append(i['url'])
    return starship_urls

pprint(collect_urls())


# pprint(response1)
# pprint(response2)
# pprint(response3)
# pprint(response4)