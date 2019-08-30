from mongoengine import fields
from mongoengine import Document

from .exercise_template import ExerciseTemplate
from .exercise import Exercise


class Workout(Document):
    name = fields.StringField()
    days = fields.ListField(fields.ListField(fields.EmbeddedDocumentField(Exercise)))


def json_to_workout_obj(json_workout):
    new_workout = Workout()

    new_workout.name = "test workout" # json_workout["name"]
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
