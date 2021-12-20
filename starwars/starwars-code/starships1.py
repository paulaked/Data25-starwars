import requests
from pprint import pprint


starship_request1 = requests.get("https://www.swapi.tech/api/starships")
starships1 = starship_request1.json()

starships_names = []
starships_url = []


def collecting_starships_and_pilots_function():
    # pprint(starships1)
    for i in starships1['results']:
        starships_names.append(['name'])
        starships_url.append(i['url'])

    starships_info = []
    for i in starships_url:
        starships_info.append(requests.get(i).json())
    # pprint(starships_info)

    pilot_urls = []
    for i in starships_info:
        pilot_urls.append(i.get('result').get('properties').get('pilots'))
    pprint(pilot_urls)

    print("----------------------------------------")

    for i in pilot_urls:
        if not i:
            pilot_urls.remove(i)
    pprint(pilot_urls)

    # pilot_info = []
    # for lists in pilot_urls:
    #     for elements in lists:
    #         pilot_info.append(requests.get(elements).json())
    # pprint(pilot_info)


collecting_starships_and_pilots_function()

#matching the pilot names to object id's in mongo
#db.create_collection("pilots")
#for i in pilot_names:
#    db.pilots.insert_one({
#           "name": i,
#           "pilot_id": db.characters.find_one({"name": i}, {"_id": 1}0
#})

#joined = db.pilots.aggregate([{
#   "$lookup": {
#       "from": "characters",
#       "localField": "name._id",
#       "foreignField": "_id",
#       "as": "matched_name",
#   }
#}])