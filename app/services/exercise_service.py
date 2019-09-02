import json
import os

from bson import ObjectId

from app import app
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


def create_exercise(name, image, video_url, body_parts, desc, steps):
    new_exercise = ExerciseTemplate()
    new_exercise.name = name

    for part in body_parts:
        new_exercise.body_parts_ids.append(part)

    new_exercise.desc = desc
    new_exercise.steps = steps

    # TODO: generate a unique name to store the image
    # import datetime

    filename = name + ".png"
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    new_exercise.img_url = '/images/exercise_images/' + filename
    new_exercise.video_url = video_url
    new_exercise.save()
    return new_exercise


def get_exercise_by_id(id_str: str) -> ExerciseTemplate:
    return ExerciseTemplate.objects(id=ObjectId(id_str)).first()


def get_exercise_by_id(obj_id: ObjectId) -> ExerciseTemplate:
    return ExerciseTemplate.objects(id=obj_id).first()

