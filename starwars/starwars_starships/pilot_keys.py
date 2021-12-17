# from upload_starships import insert_starships
import requests
import pprint as pp

ex_starship = {'MGLT': '75',
                'cargo_capacity': '100000',
                'consumables': '2 months',
                'cost_in_credits': '100000',
                'created': '2020-09-17T17:55:06.604Z',
                'crew': '4',
                'edited': '2020-09-17T17:55:06.604Z',
                'hyperdrive_rating': '0.5',
                'length': '34.37',
                'manufacturer': 'Corellian Engineering Corporation',
                'max_atmosphering_speed': '1050',
                'model': 'YT-1300 light freighter',
                'name': 'Millennium Falcon',
                'passengers': '6',
                'pilots': ['https://www.swapi.tech/api/people/13',
                           'https://www.swapi.tech/api/people/14',
                           'https://www.swapi.tech/api/people/25',
                           'https://www.swapi.tech/api/people/31'],
                'starship_class': 'Light freighter',
                'url': 'https://www.swapi.tech/api/starships/10'}

pilots = ex_starship['pilots']
pilot_list = []
for pilot in pilots:
    pilot_info = requests.get(pilot).json()['result']['properties']['name']
    pilot_list.append(pilot_info)

pp.pprint(pilot_list)

# for ship in initial_list
#     pilots = ship['pilots']

# for pilot in pilots:
#     pilot_info = requests.get(pilot)

