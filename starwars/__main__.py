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
    api = "https://www.swapi.tech/api/starships"
    api_response = get_request(api)
    response_json = make_json(api_response)
    starship_urls = collect_urls(api, response_json)
    pilot_urls_list = collect_pilot_urls(starship_urls)
    pilot_urls = only_urls(pilot_urls_list)
    pilot_names = collect_pilot_names(pilot_urls)
    pilot_object_ids = collect_object_ids(pilot_names)
    pilot_urls_object_ids_dict = create_dictionary(pilot_urls, pilot_object_ids)
    create_collection(name="starships")
    swap_urls_for_ids(starship_urls, pilot_urls_object_ids_dict)
