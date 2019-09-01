from mongoengine import fields
from mongoengine import EmbeddedDocument
from .exercise_template import ExerciseTemplate


class Exercise(EmbeddedDocument):
    exercise_id = fields.ReferenceField(ExerciseTemplate)

    sets = fields.IntField()
    reps = fields.IntField()
    time = fields.StringField()
