from app.app import get_request
from app.app import make_json
from app.app import collect_urls
from app.app import collect_pilot_urls

if __name__ == '__main__':
    api = "https://www.swapi.tech/api/starships"
    api_response = get_request(api)
    response_json = make_json(api_response)
    starship_urls = collect_urls(api, response_json)
    pilot_urls = collect_pilot_urls(starship_urls)
    print(pilot_urls)

