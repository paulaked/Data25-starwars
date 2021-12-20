import requests
from starwars.app.get_starship_url import get_api_url


def test_for_empty_list():
    url_list = get_api_url()
    not_empty = False
    if url_list:
        not_empty = True

    assert not_empty


def test_url_status():
    url_list = get_api_url()
    for i in url_list:
        assert requests.get(i) == 200


def test_is_url_starship():
    url_list = get_api_url()
    for i in url_list:
        assert requests.get(i)['result']['description'] == "A Starship"
