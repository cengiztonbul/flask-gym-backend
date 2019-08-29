from mongoengine import Document
from mongoengine import fields
from app import login


class User(Document):
    first_name = fields.StringField(required=True)
    last_name = fields.StringField(required=True)
    email = fields.EmailField(required=True, unique=True)
    role_id = fields.ObjectIdField(required=False)  # TODO Fix this, for now required=false should also add default value
    password_hash = fields.StringField(required=True)

    def get_name_obj(self):
        return {"id": str(self.id), "first_name": self.first_name, "last_name": self.last_name}


