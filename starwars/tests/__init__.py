import unittest
import pandas 
from main import get_api
from main import get_starships
from main import return_pilot
from main import insert_id
from main import insert_collection

def test_url():
    check = requests.get("https://www.swapi.tech/api/starships/")
    assert check.status_code == 200


class Testsum(unittest.TestCase)
    def test_init(self):
        result = get_api()

get_api()

GET REQUEST TO /STARSHIPS/ AND GET TOTAL_RECORDS --> STORE

RESULT = GET_API()

CHECK THAT RESULT.LENGTH === STORE.LENGTH

        
