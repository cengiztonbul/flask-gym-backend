from flask import render_template, request
from werkzeug.utils import redirect

from app.utils.login_required_role import login_required

from app.utils.forms import ExerciseForm
from app.services.exercise_service import create_exercise, get_exercise_list_json, get_exercise_by_id, get_exercise_list


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
        return get_exercise_list_json()

    @app.route('/view_exercise')
    def view_exercise():
        e_id = request.args.get('exercise_id')
        try:
            e = get_exercise_by_id(e_id)
        except:
            return redirect('/exercises')

        if e is None:
            return redirect('/exercises')

        return render_template('view_exercise.html', exercise=e.to_dict())

    @app.route('/exercises')
    def exercises():
        return render_template('exercise_list.html', exercise_list=get_exercise_list())
