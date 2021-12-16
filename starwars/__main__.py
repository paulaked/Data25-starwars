import requests
import json

if __name__ == '__main__':
    pass

API_starships = requests.get('https://www.swapi.tech/api/starships/')
print(API_starships.status_code)        #get response from api


print(API_starships.json())