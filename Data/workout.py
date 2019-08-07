from umongo import Instance, EmbeddedDocument, fields
from Data import TTDbContext as Context
from umongo import EmbeddedDocument

class Workout(EmbeddedDocument):
    pass
    class Meta:
        abstract = True
