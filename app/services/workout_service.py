import json

from bson import ObjectId

from app.models.exercise import Exercise
from app.models.exercise_template import ExerciseTemplate
from app.models.student import Student
from app.models.trainer import Trainer
from app.models.workout import Workout


def get_workout_list_by_user_id(trainer):
    e_list = []
    trainer = Trainer.objects(user_id=trainer.id).get()
    for workout_id in trainer.workout_ids:
        e_list.append(workout_id.get_name_obj())
    return json.dumps(e_list)


def json_to_workout_obj(json_workout):
    new_workout = Workout()

    new_workout.name = "test workout"  # json_workout["name"]
    for day in json_workout["days"]:
        daily_exercises = []
        for exercise in day:
            new_exercise = Exercise()
            new_exercise.exercise_id = ExerciseTemplate.objects(id=exercise["exercise"]).first()
            new_exercise.sets = int(exercise["sets"])
            new_exercise.reps = int(exercise["reps"])
            daily_exercises.append(new_exercise)
        new_workout.days.append(daily_exercises)

    new_workout.save()
    return new_workout


def find_workout_by_id(id_str: str):
    return Workout.objects(id=ObjectId(id_str)).first()


def find_workout_by_user_id(user_id):
    student = Student.objects(user_id=user_id).first()
    return student.workouts_ids[0].to_json()
