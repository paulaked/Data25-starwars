import requests
from starwars.app.get_starship_url import get_api_url


#   Function creates a list of the properties data from each starship api
#   takes the url list and iterates through
def create_starship_list():
    # get url list from get_api_url function
    url_list = get_api_url()

    starship_data_list = []
    # appending the starship properties values from url list into a list
    for url in url_list:
        starship_data_list.append((requests.get(url)).json()['result']['properties'])

    return starship_data_list
