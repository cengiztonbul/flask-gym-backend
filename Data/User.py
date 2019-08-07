from umongo import Document
from umongo import fields
from Data.workout import Workout

class Users(Document):
    last_name = fields.StringField(required=True)
    first_name = fields.StringField(required=True)
    email = fields.EmailField(required=True, unique=True)
    weight = fields.IntegerField()
    birth_date = fields.DateField()
    workout = fields.EmbeddedField(Workout)
