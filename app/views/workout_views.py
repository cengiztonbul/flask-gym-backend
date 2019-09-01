from bson import ObjectId
from flask import render_template, request
from flask_login import current_user

from app.models.student import Student
from app.services.workout_service import json_to_workout_obj, find_workout_by_id
from app.services.workout_service import get_workout_list_by_user_id
from app.utils.login_required_role import login_required


def admin_workout_routes(app):
    @app.route('/workout', methods=['GET'])
    @login_required(['admin'])
    def add_workout_get():
        return render_template("/create_workout.html")

    @app.route('/workout', methods=['POST'])
    @login_required(['admin'])
    def add_workout_post():
        data = request.json
        s = Student.objects(user_id=ObjectId(data["user_id"])).first()
        s.add_workout(json_to_workout_obj(data))
        return "ok"

    @app.route('/workout_by_id', methods=['POST'])
    @login_required(['admin'])
    def add_workout_id_post():
        data = request.json
        s = Student.objects(user_id=ObjectId(data["user_id"])).first()
        s.add_workout(find_workout_by_id(data["id"]))
        return "ok"

    @app.route('/data/workouts')
    @login_required(['admin', 'trainer'])
    def workout_list():
        return get_workout_list_by_user_id(current_user)


