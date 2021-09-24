from flask import jsonify, request
from marshmallow.exceptions import ValidationError

from webapp import app
from webapp.models import Comment, CommentSchema, Post, PostCommentsSchema, PostSchema


@app.after_request
def add_headers(resp):
    resp.headers.add('Access-Control-Allow-Origin', '*')
    resp.headers.add('Access-Control-Allow-Headers', '*')
    return resp


@app.errorhandler(ValidationError)
def marshmallow_error_handler(error):
    return error.messages, 400


@app.route("/posts/", methods=["GET"])
def get_posts():
    """ Возвращает все посты. """
    schema = PostSchema(many=True)
    posts = Post.query.all()
    return jsonify(schema.dump(posts))


@app.route("/posts/<int:post_id>/like/", methods=["POST"])
def post_like(post_id):
    """ Ставим лайк. """
    schema = PostSchema()
    post = Post.query.get_or_404(post_id)
    post.likes += 1
    post.save()
    return jsonify(schema.dump(post))


@app.route("/posts/<int:post_id>/dislike/", methods=["POST"])
def post_dislike(post_id):
    """ Ставим дизлайк. """
    schema = PostSchema()
    post = Post.query.get_or_404(post_id)
    post.dislikes += 1
    post.save()
    return jsonify(schema.dump(post))


@app.route("/posts/<int:post_id>/comments/", methods=["GET"])
def get_comments(post_id):
    """ Получаем все комментарии по посту. """
    post = Post.query.get_or_404(post_id)
    schema = PostCommentsSchema()
    return jsonify(schema.dump(post)['comments'])


@app.route("/posts/<int:post_id>/comments/", methods=["POST"])
def post_comment(post_id):
    """ Добавить комментарий к посту. Параметры: author:str, content:str. """
    post = Post.query.get_or_404(post_id)
    schema = CommentSchema()
    data = schema.load(request.get_json())
    comment = Comment(post_id=post.id, **data).add()
    return jsonify(schema.dump(comment)), 201
