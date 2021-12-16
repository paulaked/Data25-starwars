import unittest
from upload_starships import insert_starships


class test_upload(unittest.TestCase):
    def test_type(self):
        input = insert_starships("https://www.swapi.tech/api/starships/")
        answer = "<class 'list'>"
        self.assertIsInstance(input, list)  # add assertion here


if __name__ == '__main__':
    unittest.main()
