from main import *

starships5 = properties("https://www.swapi.tech/api/starships/")


for i in starships5:
    pprint(i.get('result'))
