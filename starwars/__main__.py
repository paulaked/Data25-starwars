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
    starship_properties.append(((requests.get(i).json()).get("result").get('properties')))

# print(starship_properties)

# retrieving the pilot url's from the starship properties
pilots_url = []
for i in starship_properties:
    pilots_url.append(i.get('pilots'))
pilots_url2 = [x for x in pilots_url if x]
flatList = [item for elem in pilots_url2 for item in elem]
# print(flatList)
# print(pilots_url)
pilot_names = []
for url in flatList:
    url_info = requests.get(url).json()
    pilot_id = url_info['result']['properties']['name']
    pilot_names.append(pilot_id)


mongo_ids = []
for name in pilot_names:
    mongo_id = db.characters.find_one({"name": name}, {"_id": 1})
    mongo_ids.append(mongo_id)

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

# for i in starship_properties:
#     pprint(i.get('pilots'))

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


# made dictionary with pilot url and matching id from mongoDB
pilot_dict = dict(zip(flatList, mongo_ids))
# print(pilot_dict)

db.drop_collection("starships")
db.create_collection("starships")

for i in urls_starships:
    ship_info = requests.get(i).json()
    pilot_id_list=[]
    for i in ship_info['result']['properties']['pilots']:
        if i == []:
            pass
        else:
            pilot_id_list.append(pilot_dict[i])
            ship_info['result']['properties']['pilots'] = pilot_id_list
    db.starships.insert_one(ship_info)


#
# for starship in starship_properties:
#     for property in starship:
#         if property != pilots:
#             pass
#         else:
#             list_url = []
#             for i in property:
#                 for url in pilot_dict:
#                     if i == url:
#                         list_url.append(pilot_dict[url])
#                         print(list_url)
#                 starship['pilots'] = list_url
#
# for starship in starship_properties:
#     pprint(starship)



# inserting each starship into mongoDB


# for i in starship_properties:
#     db.starships.insert_one({
#         "properties": i,
#
#
# })

# joined = db.pilots.aggregate([{
#     "$lookup": {
#         "from": "pilots",
#         "localField": "pilot_ids.pilot_id",
#         "foreignField": "pilot_id",
#         "as": "matched_name"
#     }
# }])






