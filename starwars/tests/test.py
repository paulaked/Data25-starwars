import unittest
from starwars.app.app import ApiRequest as ar
from starwars.app.app import StarshipUrls as su



class TestApiRequest(unittest.TestCase):

    def test_status_code(self):
        address = "https://www.swapi.tech/api/starships"
        status_code = ar.get_request(ar(address)).status_code
        self.assertEqual(status_code, 200)

    def test_type_dict(self):
        address = "https://www.swapi.tech/api/starships"
        data = ar.make_json(ar(address), ar.get_request(ar(address)))
        self.assertIsInstance(data, dict)


    def test_total_ship_urls(self):
        data = ar.make_json(self.a_a, a.get_request(self.a_a))
        list_length = len(s.collect_urls(self.a_a, data))
        total_records = data["total_records"]
        self.assertEqual(list_length, total_records)

if __name__ == "__main__":
    unittest.main()
