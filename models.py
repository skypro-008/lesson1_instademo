from main import db


# POST

class Post(db.Model):
    __tablename__='posts'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50))
    content = db.Column(db.String(1000))
    image = db.Column(db.String(100))
    views = db.Column(db.Integer)
    comments = db.relationship('Comment')


# COMMENT

class Comment(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100))
    content = db.Column(db.String(1000))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
