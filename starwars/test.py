# import unittest
from __main__ import *

# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here


# if __name__ == '__main__':
#     unittest.main()

def test_properties(url):
    print(properties(url))

test_properties("https://www.swapi.tech/api/starships/")