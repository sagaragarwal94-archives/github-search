from flask import render_template, request
from . import home
import requests


@home.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        org_name = request.form['search']
        #main code starts here!
        #org_name = str(raw_input("Enter the name of the organisation: ")).lower()
        api_url = "https://api.github.com/orgs/"+ org_name + "/repos"
        r= requests.get(api_url)
        json_obj = r.json()
        try:
            json_obj['message']
            context_dict = {"message":"No such organisation exists!"}
            return render_template('home/results.html',context_dict=context_dict)
        except:
            sorted_list = sorted(json_obj, key=lambda k: k['name'], reverse = False)
            return render_template('home/results.html',org_name=org_name,sorted_list=sorted_list)
    return render_template('home/index.html')
