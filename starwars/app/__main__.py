from pprint import pprint
import requests
import pymongo
if __name__ == '__main__':
    pass
response1 = requests.get('https://www.swapi.tech/api/starships/')
response2 = requests.get('https://www.swapi.tech/api/starships?page=2&limit=10')
response3 = requests.get('https://www.swapi.tech/api/starships?page=3&limit=10')
response4 = requests.get('https://www.swapi.tech/api/starships?page=4&limit=10')

starships1 = response1.json()
starships2 = response2.json()
starships3 = response3.json()
starships4 = response4.json()
pprint(starships4)



