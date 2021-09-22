from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema

from webapp import db
from webapp.mixins import SQLMixin


class Post(SQLMixin, db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50))
    content = db.Column(db.String(1000))
    image = db.Column(db.String(100))
    likes = db.Column(db.Integer, default=0)
    dislikes = db.Column(db.Integer, default=0)
    views = db.Column(db.Integer, default=0)
    comments = db.relationship('Comment', cascade="all, delete")

    def __init__(self, author: str, content: str, image: str):
        self.author = author
        self.content = content
        self.image = image


class PostSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema):
        model = Post

    id = fields.Integer(dump_only=True)
    author = fields.String(required=True)
    content = fields.String(required=True)
    image = fields.String(required=True)
    views = fields.Integer()
    likes = fields.Integer()
    dislikes = fields.Integer()
    comments = fields.Nested('CommentSchema', many=True, only=('id',))


class PostCommentsSchema(PostSchema):
    comments = fields.Nested('CommentSchema', many=True)
