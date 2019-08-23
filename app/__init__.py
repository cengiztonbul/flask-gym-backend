from flask import Flask


def create_app():
    app = Flask(__name__, static_url_path="")

    from .services import init_services
    init_services()

    from .views import init_views
    init_views(app)

    return app
