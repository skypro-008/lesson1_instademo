from flask import abort, jsonify, request
from flask_cors import cross_origin

from webapp import app
from webapp.models import Comment, Post


@app.route("/posts/", methods=["GET"])
def get_posts():
    """ Возвращает все посты. """
    response = jsonify([post.to_dict() for post in Post.query.all()])
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/posts/<int:post_id>/like/", methods=["POST"])
@cross_origin()
def post_like(post_id):
    """ Ставим лайк. """
    post = Post.query.get_or_404(post_id)
    post.likes += 1
    post.save()
    return jsonify(post.to_dict())


@app.route("/posts/<int:post_id>/dislike/", methods=["POST"])
@cross_origin()
def post_dislike(post_id):
    """ Ставим дизлайк. """
    post = Post.query.get_or_404(post_id)
    post.dislikes += 1
    post.save()
    return jsonify(post.to_dict())


@app.route("/posts/<int:post_id>/comments/", methods=["GET"])
def get_comments(post_id):
    """ Получаем все комментарии по посту. """
    post = Post.query.get_or_404(post_id)
    response = jsonify([comment.to_dict() for comment in post.comments])
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/posts/<int:post_id>/comments/", methods=["POST"])
@cross_origin()
def post_comment(post_id):
    """ Добавить комментарий к посту. Параметры: author:str, content:str. """
    post = Post.query.get_or_404(post_id)
    data: dict = request.get_json()
    if "author" not in data or "content" not in data:
        abort(400)

    comment = Comment(data['author'], data['content'], post.id).add()
    return jsonify(comment.to_dict()), 201
