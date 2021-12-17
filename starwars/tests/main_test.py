import pytest
import pandas as pd
from starwars.app.AppMain import *


# ------------------ FUNCTION 1: DROP STARSHIPS ------------------ #

# Test that drop_starships completely empties the starships collection.
def test_drop_starships():
    drop_starships()
    data = db.starships.find({})
    assert pd.notnull(data)


# ------------------ FUNCTION 2: PULL DATA ------------------ #

# Test that at least some data has been pulled from the API.
def test_pull_data():
    data = pull_data()
    assert any(data)


# ------------------ FUNCTION 3: REPLACE OBJECT IDS ------------------ #

# Test that pilots have been replaced with ObjectIDs.
def test_replace_oids():
    replace_oids()


# ------------------ FUNCTION 4: INSERT DATA ------------------ #

# Test that starships data has been inserted into the starships collection.
def test_insert_starships():
    insert_starships()
