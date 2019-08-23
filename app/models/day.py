from mongoengine import Document, fields


class Day(Document):
    daily_workout_ids = fields.ListField(fields.ObjectIdField)
