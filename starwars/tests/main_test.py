import pytest
from starwars.app.DropShips import drop_starships, db


def test_drop_starships():
    assert db.starships.find({}) != ""


