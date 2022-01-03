# Data 25 Star Wars Project ====> Ella's Branch

## Trello board

https://trello.com/invite/b/aXvLSF0v/964f40fe0f13ee1f76ea3cf1047b05ac/data25-starwars

## Instructions for use

- All functions are contained within the AppMain file in the app folder.
- Functions may be run individually (but call upon previous functions to work)
- To run all functions in one go, simply run Function 4: insert_starships()

## Functions breakdown
### Function 1: drop_starships()
Checks for any entries in an existing starships database.
<br/> Deletes these, then drops the entire database.

### Function 2: pull_data()
Sends request to the SWAPI for the starships data.
<br/> Adds each page of results in JSON format to a list.

### Function 3: replace_oids()
Extract the URLs obtained from pull_data() which link to pilot details.
<br/> For each pilot, search the characters database using their name to find their ObjectID.
<br/> Append their ObjectID to the list of pilots for that starship.

### Function 4: insert_starships()
Calls drop_starships() to eliminate any existing starships data.
<br/> Creates new starships collection.
<br/> Inserts each starship from replace_oids() into the collection.