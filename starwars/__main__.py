from app.app import StarshipUrls as s
from pprint import pprint

if __name__ == '__main__':
    api = "https://www.swapi.tech/api/starships"
    api_response = s.get_request(s(), api)
    response_json = s.make_json(s(), api_response)
    starship_urls = s.collect_urls(s(), response_json, api)

