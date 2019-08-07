from umongo import Instance, EmbeddedDocument, fields
from Data import TTDbContext as Context
from umongo import Document

instance = Instance(Context.get_db().test_database)


@instance.register
class Workout(Document):
    pass
    class Meta:
        abstract = True
