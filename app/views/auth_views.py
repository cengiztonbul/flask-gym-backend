from flask import redirect, render_template, request, flash

from app.models.user import User
from app.services.user_manager import initialize_user_for_login
from app.utils.forms import LoginForm
from flask_login import current_user, login_user, user_login_confirmed


def init_auth_views(app):

    @app.route("/login", methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if request.method == 'GET':
            return render_template("login.html", form=form)
        if form.validate_on_submit():
            u = User.objects(email=form.email.data).first()
            login_user(user=u, remember=form.remember_me.data,force=True)
            x = current_user
            print(current_user.email)

            return redirect("/")
        else:
            flash("test")
            return render_template("login.html", form=form)
        # if user is None:
        #     return redirect("/login")

    # @app.route("/login", methods=['GET'])
    # def login(request):
    #     return render_template("login.html")
