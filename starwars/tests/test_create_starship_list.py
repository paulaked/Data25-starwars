from starwars.app.create_starship_list import create_starship_list


def test_for_empty_list():
    starship_data_list = create_starship_list()
    not_empty = False
    if starship_data_list:
        not_empty = True

    assert not_empty


def test_if_dict():
    starship_data_list = create_starship_list()
    for i in starship_data_list:
        assert isinstance(i, dict)


def test_has_pilots():
    starship_data_list = create_starship_list()
    pilots = False
    for i in starship_data_list:
        if 'pilots' in i:
            pilots = True
        else:
            break
    assert pilots


def test_pilots_is_list():
    starship_data_list = create_starship_list()
    assert isinstance(starship_data_list['pilots'], list)
