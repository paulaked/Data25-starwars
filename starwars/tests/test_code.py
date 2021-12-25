from app.main_code import *

# Test passed - data in list
def test_collect_results():
    assert any(collect_results())


# Test passed - urls in list
def test_collect_urls():
    assert any(collect_urls())


# Test passed - pilot name in list
def test_change_pilot_urls_to_name():
    assert any(change_pilot_urls_to_name())


# Test passed - collection data is a dictionary
def test_upload_collection():
    for i in sw_starships.find():
        assert type(i) is dict


# Test passed - Object in pilots is a dictionary
def test_pilot_id():
    for i in sw_starships.find():
        for j in i['pilots']:
            assert type(j) is dict


