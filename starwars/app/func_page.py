# Creating functions to use APIs

import requests
import json

def api_request(url):
    raw_data = requests.get(url)
    json_data = raw_data.json()
    return(json_data)

