from motorengine import fields
from motorengine import Document
from Data.user import User
from Data.injuries import Injuries


class Student(Document):
    user_id = fields.ReferenceField(User)

    workouts_ids = fields.ListField(fields.ObjectIdField)
    diets_ids = fields.ListField(fields.ObjectIdField)
    injuries = fields.EmbeddedDocumentField(Injuries)
