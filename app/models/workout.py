from bson import ObjectId
from mongoengine import fields
from mongoengine import Document

from .exercise_template import ExerciseTemplate
from .exercise import Exercise


class Workout(Document):
    name = fields.StringField()
    days = fields.ListField(fields.ListField(fields.EmbeddedDocumentField(Exercise)))

    def get_name_obj(self):
        return {
            "name": self.name,
            "id": str(self.id)
        }


