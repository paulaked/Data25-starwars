# Author: B. Apanasionok
# Contact: B.Apanasionok@spartaglobal.com
# Date: 05/01/2022
# Revision: Final Submission
#
# this is the main file used to run a programme with the following functionality.
#   - To request the swappi starwars api and collect information stored for each starship
#   - Collect the pilot urls and names associated with each starship
#   - Collect the object ids in the characters collection stored in the starwars mongodb database.
#   - Swap the pilot urls for each ship with the equivalent object ids and store each updated starship in a new
#     collection called starships within the starwars database.
#
#
# all required functions are imported individually from the app file in the app folder.
from app.app import get_request
from app.app import make_json
from app.app import collect_urls
from app.app import collect_pilot_urls
from app.app import only_urls
from app.app import collect_pilot_names
from app.app import collect_object_ids
from app.app import create_dictionary
from app.app import create_collection
from app.app import swap_urls_for_ids

if __name__=='__main__':
    # api address for the swappi api, /starships is the location of the first page of all starship urls.
    api = "https://www.swapi.tech/api/starships"
    api_response = get_request(api)
    response_json = make_json(api_response)
    # starship urls is a list of urls, where each url is the location of information about a specific starship.
    starship_urls = collect_urls(api, response_json)
    # the url for information about each pilot is collected.
    pilot_urls_list = collect_pilot_urls(starship_urls)
    # due to pilot_urls_list being a list of lists, and empty lists where no pilots are pressent only valid urls are
    # collected and stored in a single list.
    pilot_urls = only_urls(pilot_urls_list)
    # the name of each pilot is collected using the pilot url
    pilot_names = collect_pilot_names(pilot_urls)
    # using each pilot name the corresponding object id is found
    pilot_object_ids = collect_object_ids(pilot_names)
    # a key value pair of pilot urls and object ids is created.
    pilot_urls_object_ids_dict = create_dictionary(pilot_urls, pilot_object_ids)
    # starships collection is created, and pilot urls are swapped for object ids. each starship is added as a
    # document to the starships collection.
    create_collection(name="starships")
    swap_urls_for_ids(starship_urls, pilot_urls_object_ids_dict)
