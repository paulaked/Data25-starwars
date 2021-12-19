import requests
from app.create_starship_list import create_starship_list
from app.return_pilot_id import return_pilot_id


#   Function iterates through pilot name from starship_data_list
#   requests the pilots name from the api and calls function giving pilot name, assigns the returned pilot id
#   replaces the pilot list value with the corresponding pilot id in the full starship data list
def get_name_insert_id():
    # get starship data list from create_starship_list function
    starship_data_list = create_starship_list()
    #   iterate through each starships data
    for ship_data in starship_data_list:
        #   check for populated pilot lists
        if ship_data['pilots']:
            #   iterate though each pilots api
            for pilot in ship_data['pilots']:
                #   requests pilots name and call function giving pilot name and assigns the returned pilot id
                pilot_id = return_pilot_id(requests.get(pilot).json()['result']['properties']['name'])
                #   replaces the pilot list value with the pilot id in the full starship data list
                starship_data_list[starship_data_list.index(ship_data)]['pilots'][ship_data['pilots'].index(pilot)] = pilot_id

    return starship_data_list
