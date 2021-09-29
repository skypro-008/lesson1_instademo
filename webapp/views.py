from flask import jsonify, request
from marshmallow.exceptions import ValidationError

from webapp import app
from webapp.models import CommentSchema, Post, PostCommentsSchema, PostSchema


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
    posts = Post.query.all()
    return jsonify(PostSchema(many=True).dump(posts))


@app.route("/posts/<int:post_id>/like/", methods=["POST"])
def post_like(post_id):
    """ Ставим лайк. """
    post = Post.query.get_or_404(post_id)
    post.likes += 1
    post.save()
    return jsonify(PostSchema().dump(post))


@app.route("/posts/<int:post_id>/dislike/", methods=["POST"])
def post_dislike(post_id):
    """ Ставим дизлайк. """
    post = Post.query.get_or_404(post_id)
    post.dislikes += 1
    post.save()
    return jsonify(PostSchema().dump(post))


@app.route("/posts/<int:post_id>/comments/", methods=["GET"])
def get_comments(post_id):
    """ Получаем все комментарии по посту. """
    post = Post.query.get_or_404(post_id)
    return jsonify(PostCommentsSchema().dump(post)['comments'])


@app.route("/posts/<int:post_id>/comments/", methods=["POST"])
def post_comment(post_id):
    """ Добавить комментарий к посту. Параметры: author:str, content:str. """
    post = Post.query.get_or_404(post_id)
    data = request.get_json()
    data.update(post_id=post.id)
    comment = CommentSchema().load(data).add()
    return jsonify(CommentSchema().dump(comment)), 201
