from flask import Blueprint


orgs = Blueprint('orgs', __name__)

from . import routes
