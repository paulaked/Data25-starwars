import unittest
from starwars.app.app import get_request
from starwars.app.app import make_json
from starwars.app.app import collect_urls



class TestApiRequest(unittest.TestCase):

    def test_status_code(self):
        address = "https://www.swapi.tech/api/starships"
        status_code = get_request(address).status_code
        self.assertEqual(status_code, 200)

    def test_type_dict(self):
        address = "https://www.swapi.tech/api/starships"
        data = make_json(get_request(address))
        self.assertIsInstance(data, dict)

    def test_total_starships_returned(self):
        address = "https://www.swapi.tech/api/starships"
        data = make_json(get_request(address))
        list_length = len(collect_urls(address, data))
        total_records = data["total_records"]
        self.assertEqual(list_length, total_records)

if __name__ == "__main__":
    unittest.main()
