from ..utils.login_required_role import login_required

from flask import render_template
from flask_login import current_user

from app.services.trainer_service import student_json_list, trainer_list


def admin_routes(app):
    @app.route('/admin_panel')
    @login_required(['admin'])
    def admin_panel():
        return render_template("/admin_index.html")

    @app.route('/students')
    @login_required(['admin', 'trainer'])
    def students():
        return render_template("/list_users.html")

    @app.route('/edit_profile')
    @login_required(['admin'])
    def edit_student():
        return render_template("/edit_profile.html")


def admin_data_routes(app):
    @app.route('/student_list')
    @login_required(['admin', 'trainer'])
    def student_list():
        return student_json_list(current_user)

    @app.route('/data/trainer_list')
    @login_required(['admin'])
    def trainers():
        return trainer_list()
