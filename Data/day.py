from motorengine import fields
from motorengine import Document


class Day(Document):
    daily_workout_ids = fields.ListField(fields.ObjectIdField)
