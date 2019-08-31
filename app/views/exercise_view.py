from flask import render_template

from app.utils.login_required_role import login_required

from app.utils.forms import ExerciseForm
from app.services.exercise_service import create_exercise, get_exercise_list


def exercise_views(app):
    @app.route('/create_exercise', methods=['GET'])
    @login_required(['admin'])
    def create_exercise_get():
        return render_template("/create_exercise.html")

    @app.route('/create_exercise', methods=['POST'])
    @login_required(['admin'])
    def create_exercise_post():
        # TODO: fill the function
        # form = ExerciseForm()
        # create_exercise(form.name, form.image, form.video_url)
        return "ok"

    @app.route('/data/exercises')
    def exercises_list():
        return get_exercise_list()
