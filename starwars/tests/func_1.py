import requests

url1 = "https://www.swapi.tech/api/starships/"


def collecting_info():
    starship_request1 = requests.get(url1)
    starships1 = starship_request1.json()
    return type(starships1)
