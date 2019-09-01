from flask import Flask
from flask_login import LoginManager
login = LoginManager()

UPLOAD_FOLDER = '/images/exercise_images'


def create_app():
    app = Flask(__name__, static_url_path="/", static_folder='static')
    app.config['SECRET_KEY'] = "5791628bb0b13ce0c676dfde280ba245"
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    from .services import init_services
    init_services()

    from .views import init_views
    init_views(app)
    login.init_app(app)
    return app
