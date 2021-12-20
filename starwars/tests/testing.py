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


# Test to see if the dictionary makes a dictionary
def func_four_test(key, value):
    assert type(func_page.make_dict(key, value)) is dict


def func_five_test(page_url):
    assert type(func_page.url_in_api(page_url)) is list


def func_six_test(url_list_ship):
    for i in url_list_ship:
        assert type(func_page.pilot_url_list(url_list_ship))[i] is list



# Testing - An area to test the functions are working correctly
# func_one_test(web_address)

# func_two_test("https://www.swapi.tech/api/starships/")

# func_three_test(page_url, page_contents)

# Test func_four_test
# key = ["a","b","c"]
# value = [1,2,3]
# print(func_four_test(key, value))

# Test func_five_test
# page_url = ["https://www.swapi.tech/api/starships/"]
# func_five_test(page_url)

# Test func_six_test
# url_list_ships = [func_page.url_in_api(page_url)]  # Uncomment line 52
# func_six_test(url_list_ships)