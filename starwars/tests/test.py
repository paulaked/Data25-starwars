# unit testing for functions found in the app file of the app folder for the starwars starships project.

# the unit testing module and all required functions from the app file are imported.
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
# the mongodb database is configured
client = pymongo.MongoClient()
db = client["starwars"]


class TestApiRequest(unittest.TestCase):

    # test to check that when the api is requested a 200 html status code is received
    def test_api_status_code(self):
        address = "https://www.swapi.tech/api/starships"
        status_code = get_request(address).status_code
        self.assertEqual(status_code, 200)


    # test to check that the api response is of type dictionary, this is to ensure that subsequent code will function
    # as keys in the dictionary need to be referenced.
    def test_api_response_type_dict(self):
        address = "https://www.swapi.tech/api/starships"
        data = make_json(get_request(address))
        self.assertIsInstance(data, dict)


    # test to compare the number of starships collected in the starship urls list and the total starships specified
    # on the api page. These should be equal.
    def test_total_starships_returned(self):
        address = "https://www.swapi.tech/api/starships"
        data = make_json(get_request(address))
        list_length = len(collect_urls(address, data))
        total_records = data["total_records"]
        self.assertEqual(list_length, total_records)


    # test to ensure that the starship urls collected are stored in a list for subsequent code.
    def test_starship_urls_type_list(self):
        address = "https://www.swapi.tech/api/starships"
        data = make_json(get_request(address))
        starship_urls = collect_urls(address, data)
        self.assertIsInstance(starship_urls, list)


    # the status code for a known starship url is tested to ensure the starship urls collected are valuid.
    def test_starship_status_code(self):
        address = "https://www.swapi.tech/api/starships/63"
        status_code = get_request(address).status_code
        self.assertEqual(status_code, 200)


    def test_starship_type_dict(self):
        address = "https://www.swapi.tech/api/starships/63"
        data = make_json(get_request(address))
        self.assertIsInstance(data, dict)


    # test to check that all starships were iterated when requesting data from the starship url page
    def test_total_starship_iterated(self):
        address = "https://www.swapi.tech/api/starships"
        data = make_json(get_request(address))
        starship_urls = collect_urls(address, data)
        pilot_urls = collect_pilot_urls(starship_urls)
        starship_urls_list_length = len(starship_urls)
        pilot_urls_list_length = len(pilot_urls)
        self.assertEqual(starship_urls_list_length, pilot_urls_list_length)


    # test to verify pilot urls are valid and return a 200 http code
    def test_pilot_status_code(self):
        address = "https://www.swapi.tech/api/people/10"
        status_code = get_request(address).status_code
        self.assertEqual(status_code, 200)


    # test to verify the number of starship documents added to the starwars database is equal to the total number of
    # starship urls collected.
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
        total_starships = len(starship_urls)
        self.assertEqual(total_starships, total_documents)


if __name__=="__main__":
    unittest.main()
