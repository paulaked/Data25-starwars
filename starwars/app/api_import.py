import requests
import pprint

r = requests.get("https://www.swapi.tech/api/starships")
print(r.status_code)

pprint.pprint(r.json())
