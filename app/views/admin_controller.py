from ..utils.login_required_role import login_required

from bson import ObjectId
from flask import render_template, request, jsonify
from flask_login import current_user

from app import login
from app.models.student import Student
from app.models.workout import json_to_workout_obj, find_workout_by_id
from app.services.trainer_manager import student_json_list, trainer_list, get_workout_list
from ..services.data_manager import get_exercise_list


def admin_routes(app):
    @app.route('/admin_panel')
    @login_required(['admin'])
    def admin_panel():
        return render_template("/admin_index.html")

    @app.route('/workout', methods=['GET'])
    def add_workout_get():
        return render_template("/create_workout.html")

    @app.route('/workout', methods=['POST'])
    def add_workout_post():
        data = request.json
        s = Student.objects(user_id=ObjectId(data["user_id"])).first()
        s.add_workout(json_to_workout_obj(data))
        return "ok"

    @app.route('/workout_by_id', methods=['POST'])
    def add_workout_id_post():
        data = request.json
        s = Student.objects(user_id=ObjectId(data["user_id"])).first()
        s.add_workout(find_workout_by_id(data["id"]))
        return "ok"

    @app.route('/students')
    @login_required(['admin', 'trainer'])
    def list_students():
        return render_template("/list_users.html")

    @app.route('/edit_profile')
    @login_required(['admin'])
    def edit_student():
        return render_template("/edit_profile.html")


def admin_data_routes(app):
    @app.route('/student_list')
    @login_required(['admin', 'trainer'])    
    def students():
        return student_json_list(current_user)

    @app.route('/test/trainer_list')
    @login_required(['admin'])
    def trainers():
        return trainer_list()

    @app.route('/data/exercises')
    def exercises_list():
        return get_exercise_list()

    @app.route('/data/workouts')
    def workout_list():
        return get_workout_list(current_user)
