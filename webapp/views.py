from flask import abort, jsonify, request

from webapp import app
from webapp.models import Comment, Post


# TODO как и где будем хранить посты
# TODO как будем импортировать посты в модели
# TODO  как мы храним лайкнутость и избранность
# TODO  может быть смотреть количестов просмотров
# TODO  как оставляется комментарий?
# TODO  где хранятся картинки


@app.route("/posts/", methods=["GET"])
def get_posts():
    """ Возвращает все посты. """
    posts = [post.to_dict() for post in Post.query.all()]
    return jsonify(posts)


@app.route("/posts/<int:post_id>/like/", methods=["POST"])
def post_like(post_id):
    """ Ставим лайк. """
    post = Post.query.get_or_404(post_id)
    post.likes += 1
    post.save()
    return jsonify(post.to_dict())


@app.route("/posts/<int:post_id>/dislike/", methods=["POST"])
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
    return jsonify([comment.to_dict() for comment in post.comments])


@app.route("/posts/<int:post_id>/comments/", methods=["POST"])
def post_comment(post_id):
    """ Добавить комментарий к посту. Параметры: author:str, content:str. """
    post = Post.query.get_or_404(post_id)
    data: dict = request.get_json()
    if "author" not in data or "content" not in data:
        abort(400)

    comment = Comment(data['author'], data['content'], post.id).save()
    return jsonify(comment.to_dict()), 201
