from flask import render_template
from ..services.test_post_programs import add_workout_to_student


def test_profile_view(app):
    @app.route('/test/create_workout')
    def x():
        return render_template("/create_workout.html")


def test_post_routes(app):
    @app.route('/test/post_workout', ['POST'])
    def y(request):
        if add_workout_to_student(request.get_json()):
            return "success"
        else:
            return "failed"

