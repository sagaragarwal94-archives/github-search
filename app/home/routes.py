from flask import render_template, redirect
from . import home

@home.route('/')
def index():
    return render_template('home/index.html')
