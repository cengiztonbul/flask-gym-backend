from umongo import Document, Instance
from umongo import fields
from Data import TTDbContext as Context
from Data.workout import Workout

instance = Instance(Context.get_db().test_database)


@instance.register
class Users(Document):
    last_name = fields.StringField(required=True)
    first_name = fields.StringField(required=True)
    email = fields.EmailField(required=True, unique=True)
    weight = fields.IntegerField()
    birth_date = fields.DateField()
    workout = fields.EmbeddedField()
