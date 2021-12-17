import pytest
from starwars.app.AppMain import *


# Test that drop_starships empties the starships collection.
def test_drop_starships():
    drop_starships()
    assert db.starships.find({}) != ""


# Test that data has been pulled from the API.
def test_pull_data():
    pull_data()


# Test that pilots have been replaced with ObjectIDs.
def test_replace_oids():
    replace_oids()


# Test that starships data has been inserted into the starships collection.
def test_insert_starships():
    insert_starships()
