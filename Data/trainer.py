from mongoengine import fields
from mongoengine import Document

from Data.user import User


class Trainer(Document):
    user_id = fields.ReferenceField(User)

    students_ids = fields.ListField(fields.ObjectIdField)
