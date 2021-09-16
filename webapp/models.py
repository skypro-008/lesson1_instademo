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

    def to_dict(self):
        return {
            'id': self.id,
            'author': self.author,
            'content': self.content,
            'image': self.image,
            'views': self.views,
            'likes': self.likes,
            'dislikes': self.dislikes,
            'comments': [comment.to_dict() for comment in self.comments]
        }


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

    def to_dict(self):
        return {
            'id': self.id,
            'author': self.author,
            'content': self.content,
            'post_id': self.post_id
        }
