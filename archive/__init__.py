from flask import Flask
from .config import Development, Production
from .routes import user_auth_routes
import archive.services.database_services as _database_services

def create_app(config_env):

    app = Flask(__name__)

    if config_env == 'dev':
        app.config.from_object(Development())
    else:
        app.config.from_object(Production())

    _database_services.create_database()

    #Register Blueprints
    app.register_blueprint(user_auth_routes.create_blueprint())

    @app.route("/",methods=['GET'])
    def index():
        return '<h2>App is Running</h2>'

    return app

