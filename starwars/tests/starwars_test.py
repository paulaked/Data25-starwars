import unittest
from upload_starships import insert_starships


class test_upload(unittest.TestCase):
    def test_type(self):
        input = insert_starships("https://www.swapi.tech/api/starships/")
        self.assertIsInstance(input, list)  # add assertion here

class test_pilots(unittest.TestCase):
    def test_type(self):
        input =
        self.assertIsInstance(input, str)

if __name__ == '__main__':
    unittest.main()
