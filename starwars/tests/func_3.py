import requests


def collecting_pilot_urls():
    url1 = "https://www.swapi.tech/api/starships/"
    starship_request1 = requests.get(url1)
    starships1 = starship_request1.json()

    starships_url = []
    for x in starships1['results']:
        starships_url.append(x['url'])

    starships_info = []
    for i in starships_url:
        starships_info.append(requests.get(i).json())

    pilot_urls_with_empties= []
    for i in starships_info:
        pilot_urls_with_empties.append(i.get('result').get('properties').get('pilots'))

    pilot_url_without_empties = [x for x in pilot_urls_with_empties if x]
    return pilot_url_without_empties
