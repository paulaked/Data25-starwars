import requests
from pprint import pprint

response = requests.get('https://www.swapi.tech/api/starships')
print(response.status_code)
ship = response.json()
#pprint(ship)
my_list = []
for val in ship['results']:
    for value in val.values():
        my_list.append(value)

url_list = []
for i in my_list:
    if i[0] == 'h':
        url_list.append(i)

if ship['next'] != None:
    next_page = requests.get(ship['next'])
    page_two = next_page.json()
    for item in page_two['results']:
        url_list.append(item['url'])
    if page_two['next'] != None:
        next_page3 = requests.get(page_two['next'])
        page_three = next_page3.json()
        for ul in page_three['results']:
            url_list.append(ul['url'])
        if page_three['next'] != None:
            next_page4 = requests.get(page_three['next'])
            page_four = next_page4.json()
            for n in page_four['results']:
                url_list.append(n['url'])



print(len(url_list))





