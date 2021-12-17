import pymongo
from pprint import pprint
import json
import requests
'''
plan
extract starship data
write function to read and extract dictionaries about people within the starship
output the starship data with pilots being people ID
'''
#  create a function utilising API to get data




def extract_urls(request):
    url_list = []
    if json_data_starships["next"] != None:
        page_n = requests.get(json_data_starships["next"])
