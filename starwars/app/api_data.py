import requests
import json
from pprint import pprint


starwars = requests.get("https://www.swapi.tech/api/starships/")

total_records = str(starwars.json()['total_records'])

starwars = requests.get("https://www.swapi.tech/api/starships?page=1&limit=" + total_records)

url_results_list = []

for i in starwars.json()['results']:
    url_results_list.append(i['url'])

print(url_results_list)

# for i in a['results']
# for i in star_wars.content['results']:
#     print(i)
# print(star_wars.content)

# json_file = json.dumps()