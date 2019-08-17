from mongoengine import fields
from mongoengine import Document


class Day(Document):
    daily_workout_ids = fields.ListField(fields.ObjectIdField)
