import unittest
from starwars.app.app import StarshipUrls as s

class StarshipUrlsTest(unittest.TestCase):

    def test_status_code(self):
        address = "https://www.swapi.tech/api/starships"
        status_code = s.get_request(s(), address).status_code
        self.assertEqual(status_code, 200)

    def test_type_dict(self):
        address = "https://www.swapi.tech/api/starships"
        data = s.make_json(s(), s.get_request(s(), address))
        self.assertIsInstance(data, dict)

if __name__ == "__main__":
    unittest.main()
