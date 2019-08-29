from flask import Flask
from flask_login import LoginManager

login = None


def create_app():
    global login

    app = Flask(__name__, static_url_path="/", static_folder='static')
    login = LoginManager(app)

    from .services import init_services
    init_services()

    from .views import init_views
    init_views(app)

    app.config['SECRET_KEY'] = "TEST"

    return app

