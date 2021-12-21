import unittest

from app import get_request as gr

class 

def get_request_test(address):
    check = gr.get_request(address)
    assert check.status_code == 200

