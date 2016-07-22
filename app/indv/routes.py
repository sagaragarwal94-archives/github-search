from flask import render_template, request, g, session, redirect, url_for
from . import indv
import requests
from ..apicode import apiresult
#from pprint import pprint

@indv.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass
    return render_template('orgs/index.html')
