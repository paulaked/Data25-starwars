import requests


def get_api_url():
    # star_wars = requests.get("https://www.swapi.tech/api/starships/")
    # find total number of records in API
    total_records = str(requests.get("https://www.swapi.tech/api/starships/").json()['total_records'])
    # concantenate total records to show all starships on one page
    star_wars = requests.get("https://www.swapi.tech/api/starships?page=1&limit=" + total_records)

    url_list = []
    # appending the 'results' values (individual starship urls) into a list
    for i in star_wars.json()['results']:
        url_list.append(i['url'])

    return url_list
