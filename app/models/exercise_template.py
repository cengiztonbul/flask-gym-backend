from mongoengine import fields
from mongoengine import Document


class ExerciseTemplate(Document):
    name = fields.StringField()
    body_parts_ids = fields.ListField(fields.StringField())
    img_url = fields.StringField()
    video_url = fields.StringField()
    desc = fields.StringField()
    app = fields.StringField()
    exercise_url = fields.StringField()

    def to_dict(self):
        return {
            "name": self.name,
            "id": str(self.id),
            "video_url": self.video_url,
            "img_url": self.img_url,
            "desc": self.desc,
            "app": self.app,
            "exercise_url": self.exercise_url,
            "body_parts": self.body_parts_ids
        }
