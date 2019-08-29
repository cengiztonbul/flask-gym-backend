from mongoengine import EmbeddedDocument
from mongoengine import fields


class Injuries(EmbeddedDocument):
    name = fields.StringField()
    status = fields.BooleanField()
