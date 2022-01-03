import unittest

from starwars.app.app import get_request
from starwars.app.app import make_json
from starwars.app.app import collect_urls
from starwars.app.app import collect_pilot_urls
from starwars.app.app import only_urls
from starwars.app.app import collect_pilot_names
from starwars.app.app import collect_object_ids
from starwars.app.app import create_dictionary
from starwars.app.app import create_collection
from starwars.app.app import swap_urls_for_ids

import pymongo
client = pymongo.MongoClient()
db = client["starwars"]


class TestApiRequest(unittest.TestCase):

    def test_api_status_code(self):
        address = "https://www.swapi.tech/api/starships"
        status_code = get_request(address).status_code
        self.assertEqual(status_code, 200)


    def test_api_response_type_dict(self):
        address = "https://www.swapi.tech/api/starships"
        data = make_json(get_request(address))
        self.assertIsInstance(data, dict)


    def test_total_starships_returned(self):
        address = "https://www.swapi.tech/api/starships"
        data = make_json(get_request(address))
        list_length = len(collect_urls(address, data))
        total_records = data["total_records"]
        self.assertEqual(list_length, total_records)


    def test_starship_urls_type_list(self):
        address = "https://www.swapi.tech/api/starships"
        data = make_json(get_request(address))
        starship_urls = collect_urls(address, data)
        self.assertIsInstance(starship_urls, list)


    def test_starship_status_code(self):
        address = "https://www.swapi.tech/api/starships/63"
        status_code = get_request(address).status_code
        self.assertEqual(status_code, 200)


    def test_starship_type_dict(self):
        address = "https://www.swapi.tech/api/starships/63"
        data = make_json(get_request(address))
        self.assertIsInstance(data, dict)


    def test_total_starship_iterated(self):
        address = "https://www.swapi.tech/api/starships"
        data = make_json(get_request(address))
        starship_urls = collect_urls(address, data)
        pilot_urls = collect_pilot_urls(starship_urls)
        starship_urls_list_length = len(starship_urls)
        pilot_urls_list_length = len(pilot_urls)
        self.assertEqual(starship_urls_list_length, pilot_urls_list_length)


    def test_pilot_status_code(self):
        address = "https://www.swapi.tech/api/people/10"
        status_code = get_request(address).status_code
        self.assertEqual(status_code, 200)


    def test_total_starships_created(self):
        api = "https://www.swapi.tech/api/starships"
        api_response = get_request(api)
        response_json = make_json(api_response)
        starship_urls = collect_urls(api, response_json)
        pilot_urls_list = collect_pilot_urls(starship_urls)
        pilot_urls = only_urls(pilot_urls_list)
        pilot_names = collect_pilot_names(pilot_urls)
        pilot_object_ids = collect_object_ids(pilot_names)
        pilot_urls_object_ids_dict = create_dictionary(pilot_urls, pilot_object_ids)
        create_collection(name="starships")
        swap_urls_for_ids(starship_urls, pilot_urls_object_ids_dict)
        total_documents = db.starships.count_documents({})
        total_names = len(pilot_names)
        self.assertEqual(total_names, total_documents)
\

if __name__=="__main__":
    unittest.main()
