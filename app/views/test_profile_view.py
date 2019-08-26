from flask import render_template
from ..services.test_get_programs import test_get_workout, test_get_diet


def test_profile_view(app):
    @app.route('/test')
    def x():
        return render_template("/view_programs.html")


def test_data_routes(app):
    @app.route('/test/workout_data')
    def y():
        return test_get_workout()

    @app.route('/test/diet_data')
    def a():
        return test_get_diet()
