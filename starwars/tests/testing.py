#List to test
# Check the extract data has extracted the data is in the form of a dictionary

from app import func_page


# This code test that the output is a dictionary
def func_one_test(url):
    assert type(func_page.api_request(url)) is dict


# Test to see if pages are equal, urls not equal
def func_two_test(list, data):
    assert len(list) == data["total_pages"]

