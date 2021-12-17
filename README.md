# Daniel Barnett Star Wars Project

## Objectives

The character data in your MongoDB database has been pulled from https://swapi.tech/.
As well as 'people', the API has data on starships.
Using Python, write code to pull data on all available starships from the API.
The "pilots" key contains URLs pointing to the characters who pilot the starship.
Use these to replace 'pilots' with a list of ObjectIDs from our characters collection, then insert the starships into their own collection in MongoDB.
(Make sure you drop any existing starships collections.)

## Requirements

- Use good coding principles.  That means testing, appropriate comments, good naming conventions and handling errors gracefully.
- Follow PEP 8
- Create a job board in Trello or similar to keep track of user stories.  This job board can be found at https://djew.atlassian.net/jira/core/projects/SWPD/board
- Your code should utilise functional programming OR object-oriented programming
- Use Test Driven Development: write tests first

## Extra Goals

-Create a new collection containing the data for all vehicles and reference pilots and films by their ObjectIDs
-Create a new collection containing information about the films
