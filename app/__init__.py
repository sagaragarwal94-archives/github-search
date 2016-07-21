from flask import Flask
from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint,url_prefix='/home')

    return app
