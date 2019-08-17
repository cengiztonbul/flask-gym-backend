from motorengine import fields
from motorengine import Document


class Workout(Document):
    name = fields.StringField()
    days = fields.ListField(fields.ObjectIdField)

