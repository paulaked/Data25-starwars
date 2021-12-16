import requests
from pprint import pprint


starship_request1 = requests.get("https://www.swapi.tech/api/starships")
starship_request2 = requests.get('https://www.swapi.tech/api/starships?page=2&limit=10')
starship_request3 = requests.get('https://www.swapi.tech/api/starships?page=3&limit=10')
starship_request4 = requests.get('https://www.swapi.tech/api/starships?page=4&limit=10')

starships1 = starship_request1.json()
starships2 = starship_request2.json()
starships3 = starship_request3.json()
starships4 = starship_request4.json()
starshipsjsons = [starships1, starships2, starships3, starships4]
# pprint(starshipsjsons)


# Now want it to print each starship individually
starships_names = []
starships_url = []
for x in range(0, 4):
    for i in starshipsjsons[x]['results']:
        # print(i)
        starships_names.append(i['name'])
        starships_url.append(i['url'])
# pprint(starships)

for i in starships_url:
    pprint(requests.get(i).json())
