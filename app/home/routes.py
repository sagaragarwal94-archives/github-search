from flask import render_template, request, g, session, redirect, url_for
from . import home
import requests
from ..apicode import apiresult
#from pprint import pprint

@home.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        org_name = request.form['search']
        return redirect(url_for('home.sort_by_name',org_name=org_name))
    return render_template('home/index.html')


@home.route('/SortByName/<org_name>')
def sort_by_name(org_name):
    json_obj = apiresult(org_name)
    try:
        json_obj['message']
        context_dict = {"message":"No such organisation exists!"}
        return render_template('home/results.html',context_dict=context_dict)
    except:
        sorted_list = sorted(json_obj, key=lambda k: k['name'], reverse = False)
        return render_template('home/sortbyname.html',org_name=org_name,sorted_list=sorted_list)



@home.route('/SortByDate/<org_name>')
def sort_by_date(org_name):
    json_obj = apiresult(org_name)
    sorted_list = sorted(json_obj, key=lambda k: k['created_at'], reverse = True)
    return render_template('home/sortbydate.html',org_name=org_name,sorted_list=sorted_list)
"""
    #json_obj = apiresult(org_name)
    json_dict = session.get('json_obj')
    #json_var = g.get('json_obj',None)
    pprint(json_dict)
    try:
        json_dict['message']
        context_dict = {"message":"No such organisation exists!"}
        return render_template('home/results.html',context_dict=context_dict)
    except:
        sorted_list = sorted(json_dict, key=lambda k: k['created_at'], reverse = True)
        return render_template('home/results.html',org_name=org_name,sorted_list=sorted_list)
        #return "Hi"
"""

@home.route('/SortByIssues/<org_name>')
def sort_by_issues(org_name):
    json_obj = apiresult(org_name)
    sorted_list = sorted(json_obj, key=lambda k: k['open_issues'], reverse = True)
    return render_template('home/sortbyissues.html',org_name=org_name,sorted_list=sorted_list)

"""
    json_dict = session.get('json_obj')
    #json_var = g.get('json_obj',None)
    pprint(json_dict)
    try:
        json_dict['message']
        context_dict = {"message":"No such organisation exists!"}
        return render_template('home/results.html',context_dict=context_dict)
    except:
        sorted_list = sorted(json_dict, key=lambda k: k['open_issues'], reverse = True)
        return render_template('home/results.html',org_name=org_name,sorted_list=sorted_list)
        #return "Hi"
"""
