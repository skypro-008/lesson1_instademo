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

    def to_dict(self):
        return {
            'id': self.id,
            'author': self.author,
            'content': self.content,
            'post_id': self.post_id
        }
