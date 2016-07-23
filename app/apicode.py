import requests

def apiresult(org_name):
    #'https://api.github.com/orgs/mozilla/repos?page=2&per_page=100'
    #api_url = "https://api.github.com/orgs/"+ org_name + "/repos?per_page=5"
    api_url = "https://api.github.com/orgs/"+ org_name + "/repos"
    r= requests.get(api_url)
    json_obj = r.json()
    return json_obj
