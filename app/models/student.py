from mongoengine import fields
from mongoengine import Document

from app.models.workout import Workout
from ..models.user import User
from ..models.injuries import Injuries


class Student(Document):
    user_id = fields.ReferenceField(User)

    workouts_ids = fields.ListField(fields.ReferenceField(Workout))
    diets_ids = fields.ListField(fields.ObjectIdField)
    injuries = fields.EmbeddedDocumentField(Injuries)

    def add_workout(self, workout):
        self.workouts_ids.append(workout)
        self.save()
