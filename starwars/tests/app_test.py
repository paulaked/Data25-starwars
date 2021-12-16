from app.functions import *


def test_get_from_api():
    for i in get_from_api():
        assert type(i['name']) is str


def test_collect_starships():
    for i in collect_starships():
        assert type(i['name']) is str


def test_collect_pilots():
    for i in collect_pilots():
        for j in i['pilots']:
            assert type(i) is str


def test_store_data():
    for starship in os.listdir('starships'):
        file_name = os.path.join('starships', starship)
        with open(file_name, 'r') as json_file:
            assert type(json.load(json_file)) is dict


def test_load_data():
    x = 0
    for i in db.starships.find({}):
        assert type(i) is dict


def test_reference_pilots():
    for i in db.starships.find({}):
        for j in i['pilots']:
            assert type(j) is dict


