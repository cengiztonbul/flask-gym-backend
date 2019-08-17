from mongoengine import fields
from mongoengine import Document


class Workout(Document):
    name = fields.StringField()
    days = fields.ListField(fields.ObjectIdField)

