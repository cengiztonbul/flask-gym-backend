from umongo import Document, Instance
from umongo.fields import StringField
from Data import TTDbContext as Context

instance = Instance(Context.get_db().test_database)


@instance.register
class User(Document):
    lname = StringField(required=True)
    fname = StringField(required=True)
