from flask import Flask
from .api.routes import api_routes
from .Persistance.database import init_app
from .config import Config
from .extensions import migrate, jwt, mail, db


def create_app():
    app = Flask(__name__)

    # Load Configurations
    app.config.from_object(Config)

    # Configuration of database
    init_app(app)

    # Adding extensions
    migrate.init_app(app, db)
    jwt.init_app(app)
    mail.init_app(app)

    # Adding routes
    app.register_blueprint(api_routes)

    return app
