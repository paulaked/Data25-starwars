import requests


def extract_info(api_url):
    api_url_request_json = requests.get(api_url).json()