from flask import render_template
from flask_login import current_user

from app.utils.login_required_role import login_required
from app.services.workout_service import find_workout_by_user_id


def student_program_views(app):
    @app.route('/profile')
    @login_required(['user'])
    def view_workout():
        return render_template('/view_programs.html')

    @app.route('/data/workout')
    @login_required(['user'])
    def get_workout():
        return find_workout_by_user_id(user_id=current_user.id)

