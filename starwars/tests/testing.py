# test the info extracted is of the correct type
url = "https://www.swapi.tech/api/starships/"

def test_extract_info():
    assert type(extract_info(url)) is dict