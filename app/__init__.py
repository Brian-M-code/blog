from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap

from config import config_options


db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
bootstrap = Bootstrap()


def create_app(config_name):
    
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    

    # Registering the main app Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Registering auth blueprint
    from .authentication import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = "/authenticate")
    
    # # Configure UploadSet
    # configure_uploads(app, photos)

    return app
# from app import routes