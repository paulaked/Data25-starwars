from app.functions import *


def test_get_from_api():
    assert type(get_from_api()) is list


def test_collect_starships():
    assert type(collect_starships()) is list


def test_collect_pilots():
    assert type(collect_pilots()) is list


def test_load_data():
    x = 0
    for i in db.starships.find({}):
        x += 1
    assert x == 36


def test_reference_pilots():
        for i in db.starships.find({}):
            for j in i['pilots']:
                assert type(j['_id']) == 'bson.objectid.ObjectId'


