import requests
import json
import pymongo
from pprint import pprint

client = pymongo.MongoClient()
db = client['starwars']

if __name__ == '__main__':
    pass  # Replace this with code to run your app

# import the starships data from the api


# requesting the data from the api
starship_request1 = requests.get("https://www.swapi.tech/api/starships/")
# starship_request2 = requests.get("https://www.swapi.tech/api/starships?page=2&limit=10")
# starship_request3 = requests.get("https://www.swapi.tech/api/starships?page=3&limit=10")
# starship_request4 = requests.get("https://www.swapi.tech/api/starships?page=4&limit=10")

# converting them to json files
starships1 = starship_request1.json()
# starships2 = starship_request2.json()
# starships3 = starship_request3.json()
# starships4 = starship_request4.json()

# obtaining each starship
list1 = starships1.get('results')
# list2 = starships2.get('results')
# list3 = starships3.get('results')
# list4 = starships4.get('results')
#
urls_starships = []
# obtaining the urls containing all the properties of each starship
for i in list1:
    urls_starships.append(i.get('url'))
# for i in list2:
#     urls_starships.append(i.get('url'))
# for i in list3:
#     urls_starships.append(i.get('url'))
# for i in list4:
#     urls_starships.append(i.get('url'))
# requesting the properties of each url
starship_properties = []
for i in urls_starships:
    starship_properties.append(requests.get(i).json())

pilots_url = []
for i in starship_properties:
    pilots_url.append(i.get('result').get('properties').get('pilots'))

# print(pilots_url)

# retrieving the objectid's from the pilot urls
pilot_ids = []
for i in pilots_url:
    for k in i:
        pilot_ids.append(((requests.get(k).json()).get("result").get("_id")))

