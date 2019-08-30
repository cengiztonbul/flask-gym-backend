from mongoengine import fields
from mongoengine import Document


class ExerciseTemplate(Document):
    name = fields.StringField()
    body_parts_ids = fields.ListField(fields.ObjectIdField)
    img_url = fields.StringField()
    video_url = fields.StringField()

    def to_dict(self):
        return {
            "name": self.name,
            "id": str(self.id)
        }
