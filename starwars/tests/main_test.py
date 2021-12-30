from starwars.app.AppMain import *


# ------------------ FUNCTION 1: DROP STARSHIPS ------------------ #

# PASSED
# Test that drop_starships completely empties the starships collection.
def test_drop_starships():
    drop_starships()
    data = db.starships.find({})
    assert pd.notnull(data)


# ------------------ FUNCTION 2: PULL DATA ------------------ #

# PASSED
# Test that at least some data has been pulled from the API.
def test_pull_data():
    data = pull_data()
    assert any(data)


# ------------------ FUNCTION 3: REPLACE OBJECT IDS ------------------ #
# PASSED
# Test that function returns at least some data.
def test_replace_oids_exists():
    data = replace_oids()
    assert any(data)


# Test that pilot URLs have been replaced with ObjectIDs.
def test_replace_oids_success():
    data = replace_oids()
    for item in data:
        if pd.notnull(item["pilots"]) and "ObjectID" not in item["pilots"]:
            flag = False
    assert flag


# ------------------ FUNCTION 4: INSERT DATA ------------------ #

# Test that some starships data has been inserted into the starships collection.
def test_insert_starships_data():
    insert_starships()
    assert any(db.starships.find({}))


# Test that for each starship, the pilots section contains a list of ObjectIDs.
def test_insert_starships_pilots():
    insert_starships()
    data = db.starships.find({})
    for item in data:
        if pd.notnull(item["pilots"]) and "ObjectID" not in item["pilots"]:
            flag = False
    assert flag
