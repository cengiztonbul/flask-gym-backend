from flask import redirect, render_template, request, flash


from app.models.user import User
from app.services.user_manager import create_user
from app.utils.forms import LoginForm, RegisterForm, RegisterFormTest
from flask_login import current_user, login_user, logout_user
from ..utils.login_required_role import login_required


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
    @login_required(["admin"])
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            create_user(form.first_name.data, form.last_name.data, form.email.data, "user")
            return "success"
        return render_template('register.html', form=form)

    @app.route('/register-page-test', methods=['GET', 'POST'])
    def register_page_test():
        form = RegisterFormTest()
        gender = request.form.get("gender")
        blood = request.form.get("blood")
        person_history = request.form.get("person_history")
        disorders = request.form.get("disorders")
        pregnancy = request.form.get("pregnancy")
        therapy = request.form.get("therapy")
        sugar = request.form.get("sugar")
        alcohol = request.form.get("alcohol")
        history = request.form.get("history")
        if form.validate_on_submit():
           # create_user(form.first_name.data, form.last_name.data, form.email.data, "user")
            print(form.first_name.data + " " + form.last_name.data + "" + str(form.contact.data) + " " +
                  str(form.date.data) + " " + " " + str(form.identityNo.data) + " "
                  + form.goals.data + " " + form.alergy.data + " " + form.job.data)
            print(gender, str(blood), str(disorders), str(person_history), str(pregnancy), therapy, sugar, alcohol)
            print(str(form.time1.data) + " " + str(form.time2.data))
            return "success"
        return render_template('register-page-test.html', form=form)

    @app.route("/logout")
    @login_required()
    def logout():
        logout_user()
        return redirect("/")
