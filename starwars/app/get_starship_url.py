import requests


#   Function gets the total_records from the main starship page
#   gets the data from new endpoint showing all records in one place
def get_api_url():
    # find total number of records in API
    total_records = str(requests.get("https://www.swapi.tech/api/starships/").json()['total_records'])
    # concatenate total records to show all starships on one page
    starship = requests.get("https://www.swapi.tech/api/starships?page=1&limit=" + total_records)

    url_list = []
    # appending the 'results' values (individual starship urls) into a list
    for i in starship.json()['results']:
        url_list.append(i['url'])

    return url_list
