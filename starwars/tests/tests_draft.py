from starships_functions import *
import pprint

# placeholder comment


# Test 1: Check API response

def test_api_response():
    check = requests.get("https://www.swapi.tech/api/starships/")
    assert check.status_code == 200

# pprint.pprint(test_api_response())