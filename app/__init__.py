from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from config import config_options
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


boostrap = Bootstrap()
db = SQLAlchemy()
photos = UploadSet('photos',IMAGES)
mail = Mail()

def create_app(config_name):
    #Initializing application
    app = Flask(__name__)
    
    # Create the app configuration
    app.config.from_object(config_options[config_name])

    #Initializing Flask Extensions
    mail.init_app(app)
    boostrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    
    
    # configure UploadSet
    configure_uploads(app,photos)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/auth')

    return app 