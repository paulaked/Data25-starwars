# List to test
# Check the extract data has extracted the data is in the form of a dictionary

import requests
from app import func_page


# This code test that the output is a dictionary
def func_one_test(url):
    assert type(func_page.api_request(url)) is dict


# This code tests the status code = 200
def func_two_test(url):
    check = requests.get(url)
    assert check.status_code == 200


# Test to see if pages are equal, urls not equal
def func_three_test(list, data):
    assert len(list) == data["total_pages"]


# def func_four_test():
#     assert
# Testing - An area to test the functions are working correctly
# func_one_test(web_address)

# func_two_test("https://www.swapi.tech/api/starships/")

# testing.func_three_test(page_url, page_contents)
