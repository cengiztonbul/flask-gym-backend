from mongoengine import Document
from mongoengine import fields
from flask_login import UserMixin
from app import login
import bson


@login.user_loader
def load_user(id):
    try:
        return User.objects(id=bson.objectid.ObjectId(id)).first()
    except:
        return None


class User(Document, UserMixin):
    first_name = fields.StringField(required=True)
    last_name = fields.StringField(required=True)
    email = fields.EmailField(required=True, unique=True)
    role = fields.StringField(required=False, default="user")
    password_hash = fields.StringField(required=True)

    def get_name_obj(self):
        return {"id": str(self.id), "first_name": self.first_name, "last_name": self.last_name}
