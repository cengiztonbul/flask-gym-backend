from flask import render_template
from ..services.test_get_programs import test_get_workout, test_get_diet


def test_profile_view(app):
    @app.route('/test/profile')
    def page():
        return render_template("/view_programs.html")

    @app.route('/test/create_workout')
    def page_2():
        return render_template("/create_workout.html")


def test_data_routes(app):
    @app.route('/test/workout_data')
    def workout_data():
        return test_get_workout()

    @app.route('/test/diet_data')
    def diet_data():
        return test_get_diet()

    @app.route('/data/d')
    def diet_data():
        return test_get_diet()
