from flask import render_template, request, redirect
from ..utils.forms import LoginForm, RegisterForm


def init_view(app):
    @app.route('/', methods=['GET'])
    @app.route('/index')
    def index():
        return render_template('index.html')

    @app.route('/users/<int:user_id>')
    def user_profile(user_id):
        return render_template('index.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if request.method == 'GET':
            return render_template('login.html', form=form)

        if form.validate_on_submit():
            return "test"
        else:
            return redirect("/login")

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            return "test"
        return render_template('register.html', form=form)

    @app.route('/logout')
    def logout():
        raise NotImplemented
