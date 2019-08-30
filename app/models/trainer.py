from mongoengine import fields
from mongoengine import Document

from ..models.workout import Workout
from ..models.user import User
from ..models.student import Student


class Trainer(Document):
    user_id = fields.ReferenceField(User)
    student_ids = fields.ListField(fields.ReferenceField(Student))
    workout_ids = fields.ListField(fields.ReferenceField(Workout))

    def add_student(self, student_id):
        self.student_ids.append(student_id)
        self.save()
