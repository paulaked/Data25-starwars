# API testing space.
import requests
import json
from pprint import pprint

starwars_people = requests.get("https://www.swapi.tech/api/people")
json_people = starwars_people.json()
#pprint(starwars_people.json())

raw_starships = requests.get("https://www.swapi.tech/api/starships")
json_starships = raw_starships.json()

# for i in json_starships["results"]:
#     print(i["url"])
# pprint(json_starships)

print(json_starships["next"])

# for i in json_starships:
#     if json_starships["next"] != None:
#         requests.get(i["next"])
#     print(i["url"])

# for i in json_starships["results"]:
#     if 'next' != None:
#         requests.get(i["next"])
#     print(i['url'])


# pprint(json_starship.status_code) # Produces 200



