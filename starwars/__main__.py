import requests
import json
import pymongo
from pprint import pprint
# from collections import Iterable
# def flatten(lis):
#      for item in lis:
#          if isinstance(item, Iterable) and not isinstance(item, str):
#              for x in flatten(item):
#                  yield x
#          else:
#              yield item

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
    starship_properties.append(((requests.get(i).json()).get("result").get('properties')))

pilots_url = []
for i in starship_properties:
    pilots_url.append(i.get('pilots'))
pilots_url2 = [x for x in pilots_url if x]
flatList = [item for elem in pilots_url2 for item in elem]
# print(flatList)

# #
# print(pilots_url)

# retrieving the name's from the pilot urls
pilot_names = []
for i in pilots_url:
    for k in i:
        pilot_names.append((((requests.get(k).json()).get("result")).get("properties").get("name")))

# retrieving the objectId's from the pilot urls
pilot_ids = []
for i in pilots_url:
    for k in i:
        pilot_ids.append((((requests.get(k).json()).get("result")).get("_id")))
# pprint(pilot_ids)


# matching the pilot names to the objct id's in mongoDB
# db.create_collection("pilots")
# for i in pilot_names:
#     db.pilots.insert_one({
#         "name": i,
#         "pilot_id": db.characters.find_one({"name": i}, {"_id": 1})
# })
#
# joined = db.pilots.aggregate([{
#     "$lookup": {
#         "from": "characters",
#         "localField": "name._id",
#         "foreignField": "_id",
#         "as": "matched_name"
#     }
# }])
# for pilot in db.pilots.find({}):
#     print(pilot)

# made dictionary with pilot url and matching id from mongoDB
pilot_dict = dict(zip(flatList, pilot_ids))
print(pilot_dict)

# for i in pilots_url:
#     pilot_info = {
#         db.pilots.find_one("pilot_id._id"): i
#     }

# def properties(api_url):
#     url_list=[]
#     api_url_request_json = requests.get(api_url).json()
#     results = api_url_request_json.get('results')
#     for i in results:
#         url_list.append(i.get('url'))
#     for i in url_list:
#         print(((requests.get(i).json()).get("result").get('properties')))

