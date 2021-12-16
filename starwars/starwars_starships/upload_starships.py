import requests
import pprint as pp

starships_id2 = requests.get("https://www.swapi.tech/api/starships/2")
starships_id3 = requests.get("https://www.swapi.tech/api/starships/3")
starships_id5 = requests.get("https://www.swapi.tech/api/starships/5")
starships_id9 = requests.get("https://www.swapi.tech/api/starships/9")
starships_id10 = requests.get("https://www.swapi.tech/api/starships/10")
starships_id11 = requests.get("https://www.swapi.tech/api/starships/11")
starships_id12 = requests.get("https://www.swapi.tech/api/starships/12")
starships_id13 = requests.get("https://www.swapi.tech/api/starships/13")
starships_id15 = requests.get("https://www.swapi.tech/api/starships/15")
starships_id17 = requests.get("https://www.swapi.tech/api/starships/17")

ss_id2 = (starships_id2.json()['result']['properties'])
ss_id3 = (starships_id3.json()['result']['properties'])
ss_id5 = (starships_id5.json()['result']['properties'])
ss_id9 = (starships_id9.json()['result']['properties'])
ss_id10 = (starships_id10.json()['result']['properties'])
ss_id11 = (starships_id11.json()['result']['properties'])
ss_id12 = (starships_id12.json()['result']['properties'])
ss_id13 = (starships_id13.json()['result']['properties'])
ss_id15 = (starships_id15.json()['result']['properties'])
ss_id17 = (starships_id17.json()['result']['properties'])