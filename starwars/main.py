# Main file for final code

from app import func_page
from pprint import pprint

# pprint(func_page.api_request("https://www.swapi.tech/api/people"))

starship_data = func_page.api_request("https://www.swapi.tech/api/people")

#pprint(func_page.extract_url(starship_data))