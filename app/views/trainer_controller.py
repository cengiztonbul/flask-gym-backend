from flask import render_template
from ..services.trainer_manager import student_json_list, trainer_test, trainer_list, register_user


def list_student_view(app):
    @app.route('/test/list_student')
    def list_student():
        return render_template("/list_users.html")

    @app.route('/test/edit_profile')
    def edit_student():
        return render_template("/edit_profile.html")

    @app.route('/test/workout')
    def workout():
        return render_template("/create_workout.html")

    @app.route('/test/add_student', methods=['GET'])
    def add_student_get():
        return render_template("/create_workout.html")

    @app.route('/test/add_student', methods=['POST'])
    def add_student_post(request):
        # noinspection PyBroadException
        try:
            register_user(request.form.get("first_name"), request.form.get("last_name"), request.form.get("email"),
                          request.form.get("trainer"))
            return 0
        except Exception:
            return -1


def students_data(app):
    @app.route('/test/trainer_list')
    def trainers():
        return trainer_list()
