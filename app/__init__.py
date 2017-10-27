from flask import Flask

def create_app(config_name):
    app = Flask(__name__)

    from .orgs import orgs as orgs_blueprint
    app.register_blueprint(orgs_blueprint)
    
    from .indv import indv as indv_blueprint
    app.register_blueprint(indv_blueprint,url_prefix='/indv')

    return app
