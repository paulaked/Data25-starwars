import requests
import json

if __name__ == '__main__':
    pass

api_data = requests.get('https://www.swapi.tech/api/starships/')
data = api_data.json()
data1 = data["results"]
print(type(data1))
print(type(data1[1]))
for i in data1:
    print(i["url"])



