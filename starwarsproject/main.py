# import the starships data from the api
import requests
import json
import pymongo
from pprint import pprint

# requesting the data from the api
starship_request1 = requests.get("https://www.swapi.tech/api/starships/")
starship_request2 = requests.get("https://www.swapi.tech/api/starships?page=2&limit=10")
starship_request3 = requests.get("https://www.swapi.tech/api/starships?page=3&limit=10")
starship_request4 = requests.get("https://www.swapi.tech/api/starships?page=4&limit=10")

# converting them to json files
starships1 = starship_request1.json()
starships2 = starship_request2.json()
starships3 = starship_request3.json()
starships4 = starship_request4.json()

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

for i in starship_properties:
    pprint(i.get('result').get('properties').get('pilots'))

# def properties(api_url):
#     url_list=[]
#     api_url_request_json = requests.get(api_url).json()
#     results = api_url_request_json.get('results')
#     for i in results:
#         url_list.append(i.get('url'))
#     starship_properties=[]
#     for i in url_list:
#         starship_properties.append(requests.get(i).json())



