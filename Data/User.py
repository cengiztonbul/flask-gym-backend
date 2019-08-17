from motorengine import fields
from motorengine import Document


class User(Document):
    first_name = fields.StringField(required=True)
    last_name = fields.StringField(required=True)
    email = fields.EmailField(required=True, unique=True)


