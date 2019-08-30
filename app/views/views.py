from flask import render_template, request, redirect
from ..utils.forms import LoginForm, RegisterForm
from ..services.user_manager import create_user
from flask_login import login_required


def init_view(app):
    @app.route('/', methods=['GET'])
    @app.route('/index')
    def index():
        return render_template('index.html')

    @app.route('/users/<int:user_id>')
    def user_profile(user_id):
        return render_template('index.html')

    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html', error=error)

    @app.errorhandler(401)
    def unauthorized(error):
        return render_template('404.html', error=error)  # TODO change to a 401 page?
