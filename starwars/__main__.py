from app import get_request
from app import get_starship_urls

if __name__ == '__main__':
    api = "https://www.swapi.tech/api/starships"

    starships_data = get_request.get_request(api)

    starship_urls_list = get_starship_urls.get_starship_urls(starships_data)
