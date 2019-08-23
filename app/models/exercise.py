from mongoengine import fields
from mongoengine import Document
from Data.exercise_template import ExerciseTemplate


class Exercise(Document):
    exercise_id = fields.ReferenceField(ExerciseTemplate)

    sets = fields.IntField()
    reps = fields.IntField()
    time = fields.StringField()
