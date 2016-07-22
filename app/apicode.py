import requests

def apiresult(org_name):
    api_url = "https://api.github.com/orgs/"+ org_name + "/repos"
    r= requests.get(api_url)
    json_obj = r.json()
    return json_obj
