import requests
import json

# Starship data is spread across different pages
# number of pages = 4
response1 = requests.get('https://www.swapi.tech/api/starships/')
response2 = requests.get('https://www.swapi.tech/api/starships?page=2&limit=10')
response3 = requests.get('https://www.swapi.tech/api/starships?page=3&limit=10')
response4 = requests.get('https://www.swapi.tech/api/starships?page=4&limit=10')
print(response1.status_code)


# Convert the data into JSON format
p1 = response1.json()
print(p1)

p2 = response2.json()
print(p2)

p3 = response3.json()
print(p3)

p4 = response4.json()
print(p4)


# Make data into a formatted string (presented as dictionaries) using the dumps() function
pp1 = json.dumps(p1, sort_keys=False, indent=2)
print(pp1)

pp2 = json.dumps(p2, sort_keys=False, indent=2)
print(pp2)

pp3 = json.dumps(p3, sort_keys=False, indent=2)
print(pp3)

pp4 = json.dumps(p4, sort_keys=False, indent=2)
print(pp4)
