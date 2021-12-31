from mini_project import *

def test_the_source():
    assert extract_data(web_address) == dict(extract_data(web_address))

def test_the_page_urls():
    assert get_url_for_all_pages() == list(get_url_for_all_pages())

def test_the_pilots_id():
    assert get_and_replace_pilots_id() == list(get_and_replace_pilots_id())

