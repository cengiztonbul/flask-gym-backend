from flask import render_template, request, redirect
from ..utils.forms import LoginForm, RegisterForm
from ..services.user_manager import create_user
from flask_login import login_required, current_user


def init_view(app):
    @app.route('/', methods=['GET'])
    @app.route('/index')
    def index():
        try:
            print(current_user.email)
        except Exception as e:
            print(e)
        return render_template('index.html')

    @app.route('/users/<int:user_id>')
    def user_profile(user_id):
        return render_template('index.html')
