import json

from bson import ObjectId

from ..models.trainer import Trainer
from ..services.user_manager import find_user_by_email, create_user

trainer_test = Trainer.objects(user_id=find_user_by_email("admin@gmail.com")).get()


def student_json_list(trainer):
    trainer = Trainer.objects(user_id=ObjectId(trainer.id)).first()
    print(trainer)
    users = []
    for s_id in trainer.student_ids:
        print(s_id.user_id)
        users.append(s_id.user_id.get_name_obj())

    return json.dumps(users)  # id_list_to_json(user_ids)


def trainer_list():
    trainers = []
    for trainer in Trainer.objects():
        trainers.append(trainer.user_id.get_name_obj())

    return json.dumps(trainers)


def register_user(first_name, last_name, email, trainer_id):
    new_user = create_user(first_name, last_name, email)
    trainer = Trainer.objects(id=trainer_id).get()
    trainer.add_student(new_user)


def get_workout_list(trainer):
    e_list = []
    trainer = Trainer.objects(user_id=trainer.id).get()
    for workout_id in trainer.workout_ids:
        e_list.append(workout_id.get_name_obj())
    return json.dumps(e_list)
