import requests

def wiki_visits(keyword, begin_date, end_date):
    #TODO: Check keyword writing and date writing
    request_url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/de.wikipedia/all-access/user/"
    request_url = request_url + keyword
    request_url = request_url + "/daily/"
    request_url = request_url + begin_date + "/"
    request_url = request_url + end_date
    r = requests.get(request_url)
    if r.status_code == 200:
        data = r.json()
        return data
    else:
        print("Error: could not fetch data from wiki for keyword: ", keyword)
        return

