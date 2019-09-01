import json
import os

from bson import ObjectId

import app
from ..models.exercise_template import ExerciseTemplate


def get_exercise_list_json():
    e_list = []
    for e in ExerciseTemplate.objects():
        e_list.append(e.to_dict())
    return json.dumps(e_list)


def get_exercise_list():
    e_list = []
    for e in ExerciseTemplate.objects():
        e_list.append(e.to_dict())
    return e_list


def create_exercise(name, image, video_url, body_parts, desc, application):
    """ application is stored with /s to split the steps. it will
    be handled on frontend"""

    new_exercise = ExerciseTemplate()
    new_exercise.name = name

    for part in body_parts:
        new_exercise.body_parts_ids.append(part)

    new_exercise.desc = desc
    new_exercise.app = application

    # generate a unique name to store the image
    import datetime
    filename = name + ".png"

    new_exercise.img_url = os.path.join("/images/exercise_images", filename)
    image.save(new_exercise.img_url)

    new_exercise.video_url = video_url
    new_exercise.save()
    return new_exercise


def get_exercise_by_id(id_str: str) -> ExerciseTemplate:
    return ExerciseTemplate.objects(id=ObjectId(id_str)).first()


def get_exercise_by_id(obj_id: ObjectId) -> ExerciseTemplate:
    return ExerciseTemplate.objects(id=obj_id).first()
