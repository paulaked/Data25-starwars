import requests
import pprint as pp


# insert_starships is a function that collects the urls of the starship api, formats them and
# appends them to a list

def insert_starships(url_link):
    initial_list = []
    url_ending = [2, 3, 5, 9, 10, 11, 12, 13, 15, 17]

    for n in url_ending:
        new_starship = requests.get(url_link + str(n))
        initial_list.append(new_starship.json()['result']['properties'])

    return initial_list


pp.pprint(insert_starships("https://www.swapi.tech/api/starships/"))
