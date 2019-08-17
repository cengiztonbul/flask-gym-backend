from motorengine import fields
from motorengine import Document


class ExerciseTemplate(Document):
    name = fields.StringField()
    body_parts_ids = fields.ListField(fields.ObjectIdField)
    img_url = fields.StringField()
    video_url = fields.StringField()

