# import unittest
from __main__ import *
import requests
from pprint import pprint

# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here


# if __name__ == '__main__':
#     unittest.main()
def properties(api_url):
    url_list=[]
    api_url_request_json = requests.get(api_url).json()
    results = api_url_request_json.get('results')
    for i in results:
        url_list.append(i.get('url'))
    starship_properties=[]
    for i in url_list:
        starship_properties.append((requests.get(i).json()).get("result"))
        pprint(starship_properties)

def extract_pilot_url(starship_properties):
    pilots_url=[]
    for i in starship_properties:
        pilots_url.append(i.get("pilots"))
    pilots_url2 = [x for x in pilots_url if x]
    flatList = [item for elem in pilots_url2 for item in elem]

def extract_pilot_names(pilots_url):
    for i in pilots_url:
        for k in i:
            pilot_names.append((((requests.get(k).json()).get("result")).get("properties").get("name")))

def extract_pilot_ids(pilots_url):
    pilot_ids = []
    for i in pilots_url:
        for k in i:
            pilot_ids.append((((requests.get(k).json()).get("result")).get("_id")))

def pilot_dict(flatList, pilot_ids):
    pilot_dict = dict(zip(flatList, pilot_ids))
    print(pilot_dict)

def test_properties():
    assert properties("https://www.swapi.tech/api/starships/")


def extract_info(api_url):
    api_url_request_json = requests.get(api_url).json()


# test the info extracted is of the correct type
url = "https://www.swapi.tech/api/starships/"

def test_extract_info():
    assert type(extract_info(url)) is dict