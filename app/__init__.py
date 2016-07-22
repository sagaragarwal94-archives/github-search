from flask import Flask
from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from .orgs import orgs as orgs_blueprint
    app.register_blueprint(orgs_blueprint,url_prefix='/orgs')
    from .indv import indv as indv_blueprint
    app.register_blueprint(indv_blueprint,url_prefix='/indv')

    return app
