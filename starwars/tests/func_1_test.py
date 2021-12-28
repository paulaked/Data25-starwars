import func_1
from pprint import pprint

url = "https://www.swapi.tech/api/starships/"

if func_1.collecting_info() is dict:
    print("func_1 passed")
else:
    print("func_1 failed")