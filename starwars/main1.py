'''
plan
extract starship data
write function to read and extract dictionaries about people within the starship
output the starship data with pilots being people ID
'''

#  imports
from app import function_list
from pprint import pprint



variable = function_list.extract_data("https://www.swapi.tech/api/starships")
pprint(function_list.extract_all_pages(variable))



