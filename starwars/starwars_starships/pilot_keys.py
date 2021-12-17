from upload_starships import insert_starships
import requests
import pprint as pp


def insert_pilots(starships_list):
    for ship in starships_list:
        if ship['pilots'] == []:
            pass
        else:
            pilots = ship['pilots']
            pilot_list = []
            for pilot in pilots:
                pilot_info = requests.get(pilot).json()['result']['properties']['name']
                pilot_list.append(pilot_info)
            ship['pilots'] = pilot_list

    return starships_list


print(insert_pilots(insert_starships("https://www.swapi.tech/api/starships/")))
