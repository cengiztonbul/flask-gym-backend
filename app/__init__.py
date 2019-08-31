from flask import Flask
from flask_login import LoginManager
from flask_user import UserManager

login = LoginManager()

# UPLOAD_FOLDER = '/images/exercise_images'


def create_app():
    app = Flask(__name__, static_url_path="/", static_folder='static')
    app.config['SECRET_KEY'] = "5791628bb0b13ce0c676dfde280ba245"
    app.config['TESTING'] = True
    print("[create_app]: config is set")
    app = Flask(__name__)
#    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    from .services import init_services
    init_services()

    from .views import init_views
    init_views(app)
    login.init_app(app)
    login.login_view = 'login'
    return app
