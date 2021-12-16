import requests
from pprint import pprint

response = requests.get('https://www.swapi.tech/api/starships')
print(response.status_code)
ship = response.json()
pprint(ship)
my_list = []
for val in ship['results']:
    for value in val.values():
        my_list.append(value)
        print(len(my_list))

#print(len(my_list))
    #print(val, type(val))
#for key in ship.keys():
    #print(key)
