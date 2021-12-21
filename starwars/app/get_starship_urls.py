# Function that returns a list of starship urls
# from the swappi api starships page

def get_starship_urls(starships_data):
    starship_urls_list = []
    for result in starships_data["results"]:
        starship_urls_list.append(result["url"])
    return starship_urls_list