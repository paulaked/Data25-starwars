import requests


def collecting_starship_urls():
    url1 = "https://www.swapi.tech/api/starships/"
    starship_request1 = requests.get(url1)
    starships1 = starship_request1.json()

    starships_url = []
    for x in starships1['results']:
        starships_url.append(x['url'])
    return type(starships_url)


