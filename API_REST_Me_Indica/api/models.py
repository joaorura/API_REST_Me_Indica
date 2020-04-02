from mongoengine import Document, fields


class LogicQuestion(Document):
    text = fields.StringField(required=True)
    imgs = fields.ListField(fields.StringField(), required=True)
    alternatives = fields.ListField(fields.StringField(), required=True)
    answer = fields.IntField(required=True)
    level = fields.IntField(required=True)
    time = fields.IntField(required=True)
