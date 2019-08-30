from flask import redirect, render_template, request, flash

from app.models.user import User
from app.services.user_manager import create_user
from app.utils.forms import LoginForm, RegisterForm
from flask_login import current_user, login_user, login_required, logout_user


def init_auth_views(app):
    @app.route("/login", methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if request.method == 'GET':
            return render_template("login.html", form=form)
        if form.validate_on_submit():
            u = User.objects(email=form.email.data).first()
            login_user(user=u, remember=form.remember_me.data)
            return redirect("/")
        else:
            flash("test")
            return render_template("login.html", form=form)

    @app.route('/register', methods=['GET', 'POST'])
    @login_required
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            create_user(form.first_name.data, form.last_name.data, form.email.data, "user")
            return "success"
        return render_template('register.html', form=form)

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        return redirect("/")
