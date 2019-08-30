import json

from ..models.exercise_template import ExerciseTemplate


def get_exercise_list():
    e_list = []
    for e in ExerciseTemplate.objects():
        e_list.append(e.to_dict())
    return json.dumps(e_list)
