# API testing space.
import requests
import json
from pprint import pprint

# starwars_people = requests.get("https://www.swapi.tech/api/people")
# json_people = starwars_people.json()
# pprint(star_wars_people.json())

raw_starships = requests.get("https://www.swapi.tech/api/starships")
json_starships = raw_starships.json()
pprint(json_starships)

# pprint(ship.status_code) # Produces 200

# with open("starships_API_URLs.json", "w") as jsonfile:
#     json.dump(star_wars_ships, jsonfile)

# ships = []
# for ship in star_wars_ships:
#     print(ship)
#     ships.append(ship)
# pprint(len(ships))



