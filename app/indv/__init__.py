from flask import Blueprint

indv = Blueprint('indv', __name__)

from . import routes
