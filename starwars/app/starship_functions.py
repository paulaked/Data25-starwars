import requests
import pprint
import json

def get_raw_starships():

    starship_requests_raw = requests.get("https://www.swapi.tech/api/starships/")
    #print(r.status_code)
    #pprint.pprint(starship_requests.json())
    starships_count = str(starship_requests_raw.json()['total_records'])  # identifies 36 starships
    # returns starships_count and so identifies number of urls to scrape
    url_list = []
    starships_urls = requests.get(f"https://www.swapi.tech/api/starships?page=1&limit={starships_count}")
    for url in starships_urls.json()['results']:
        url_list.append(url['url'])  #returns a list of urls containing the starship data
    return url_list
    
# pprint.pprint(get_raw_starships())

def get_relavent_info():
    starship_data = []
    for url in get_raw_starships():
        starship_data.append(requests.get(url).json()['result']['properties']) 
    return starship_data
    # returns json containing information in the 'properties' category

# pprint.pprint(get_relavent_info())

def get_starships_with_pilots():
    starships_with_pilots_data = []
    
