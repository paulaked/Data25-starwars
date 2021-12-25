from app.main_code import *

def test_collect_results():
    assert any(collect_results())

def test_collect_urls():
    assert any(collect_urls())

def test_change_pilot_urls_to_name():
    assert any(change_pilot_urls_to_name())

def test_upload_collection():
    for i in sw_starships.find():
        assert type(i) is dict

def test_pilot_id():
    for i in sw_starships.find():
        for j in i['pilots']:
            assert type(j) is dict


