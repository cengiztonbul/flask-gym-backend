from flask import redirect, render_template, request, flash, url_for

from app.models.user import User
from app.services.user_manager import create_user, find_user_by_email, change_user_password
from app.utils.forms import NewPasswordForm
from flask_login import current_user
from ..utils.login_required_role import login_required


def init_user_views(app):
    @app.route("/profile", methods=['GET'])
    @login_required()
    def profile():
        raise NotImplemented

    @app.route("/profile/change_password", methods=['GET', 'POST'])
    @login_required()
    def change_password():
        form = NewPasswordForm()
        if request.method == 'GET':
            return render_template('change_password.html', form=form)
        if form.validate_on_submit():
            change_user_password(email=current_user.email, password=form.new_password.data)
            return "Password Changed"
        else:
            return "failed the check"
