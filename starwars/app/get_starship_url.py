import requests
import starwars.config_manager as config


#   Function gets the total_records from the main starship page
#   gets the data from new endpoint showing all records in one place
def get_api_url():
    # find total number of records in API
    total_records = str(requests.get(f"{config.SWAPI_URL}/api/starships/").json()['total_records'])
    # concatenate total records to show all starships on one page
    starships = requests.get(f"{config.SWAPI_URL}/api/starships?page=1&limit=" + total_records)

    url_list = []
    # appending the 'results' values (starship urls) to a list
    for starship in starships.json()['results']:
        url_list.append(starship['url'])

    return url_list
