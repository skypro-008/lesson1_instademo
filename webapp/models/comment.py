from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema

from webapp import db
from webapp.mixins import SQLMixin


class Comment(SQLMixin, db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100))
    content = db.Column(db.String(1000))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def __init__(self, author: str, content: str, post_id: int):
        self.author = author
        self.content = content
        self.post_id = post_id


class CommentSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema):
        model = Comment

    id = fields.Integer(dump_only=True)
    author = fields.String(required=True)
    content = fields.String(required=True)
    post_id = fields.Integer()
