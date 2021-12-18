import requests
from get_starship_url import get_api_url


def create_starship_list():
    # get url list from get_api_url function
    url_list = get_api_url()

    starship_list = []
    # appending the starship properties values from url list into a list
    for i in url_list:
        starship_list.append((requests.get(i)).json()['result']['properties'])

    return starship_list
