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

    # @app.route('/login', methods=['GET', 'POST'])
    # def login():
    #     form = LoginForm()
    #     if request.method == 'GET':
    #         return render_template('login.html', form=form)
    #
    #     if form.validate_on_submit():
    #         return "test"
    #     else:
    #         return redirect("/login")

    @app.route('/register', methods=['GET', 'POST'])
    @login_required
    def register():
        print("-----")
        print(current_user.email)
        print("-----")
        form = RegisterForm()
        if form.validate_on_submit():
            create_user(form.first_name.data, form.last_name.data, form.email.data, "user")
            return "success"
        return render_template('register.html', form=form)

    @app.route('/logout')
    def logout():
        raise NotImplemented
