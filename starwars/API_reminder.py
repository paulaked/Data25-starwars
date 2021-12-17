# API testing space.
import requests
import json
from pprint import pprint

starwars_people = requests.get("https://www.swapi.tech/api/people")
json_people = starwars_people.json()

raw_starships = requests.get("https://www.swapi.tech/api/starships")
json_starships = raw_starships.json()

starships_url = []
for i in json_starships["results"]:
    starships_url.append(i["url"])

if json_starships["next"] != None:
    raw_starships_page2 = requests.get(json_starships["next"])
    json_starships_page2 = raw_starships_page2.json()
    for i in json_starships_page2["results"]:
        starships_url.append(i["url"])
    if json_starships_page2["next"] != None:
        raw_starships_page3 = requests.get(json_starships_page2["next"])
        json_starships_page3 = raw_starships_page3.json()
        for j in json_starships_page3["results"]:
            starships_url.append(j["url"])
        if json_starships_page3["next"] != None:
            raw_starships_page4 = requests.get(json_starships_page3["next"])
            json_starships_page4 = raw_starships_page4.json()
            for k in json_starships_page4["results"]:
                starships_url.append(k["url"])

#print(starships_url)


# def calling_url(requests):
#     url_list = []
#     if json_starships["next"] != None:



# for i in starships_url:
#     file = requests.get(i)
#     print(file.json())







# for i in json_starships:
#     if json_starships["next"] != None:
#         requests.get(i["next"])


# for i in json_starships:
#     if json_starships["next"] != None:
#         requests.get(i["next"])
#     print(i["url"])

# for i in json_starships["results"]:
#     if 'next' != None:
#         requests.get(i["next"])
#     print(i['url'])


# pprint(json_starship.status_code) # Produces 200



