from flask import Flask


def create_app():
    app = Flask(__name__, static_url_path="")

    from .services import init_services
    init_services()


    return app
