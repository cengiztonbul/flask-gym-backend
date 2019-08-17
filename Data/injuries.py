from mongoengine import Document
from mongoengine import fields


class Injuries(Document):
    name = fields.StringField()
    status = fields.BooleanField()
