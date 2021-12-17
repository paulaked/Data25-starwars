import requests

from app import function_list
api_address = "https://www.swapi.tech/api/starships"
web_address = api_address

#  Testing output of above
def test_extract_data(url):
    assert type(function_list.extract_data(web_address)) is dict
#  If process finished with exit code 0, api works.

#  Test code pulls different page urls by comparing first to last
assert web_address[0] != web_address[3]
#  If process finished with exit code 0, test pulls different urls.

