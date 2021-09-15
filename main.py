import os

from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Post, Comment  # noqa

""" ПОСТЫ """


@app.route("/posts/")
def get_posts():
    posts = Post.query.all()
    print(posts)
    return jsonify({})
    """Возвращает список всех постов"""

    # TODO как и где будем хранить посты
    # TODO как будем импортировать посты в модели
    # TODO  как мы храним лайкнутость и избранность
    # TODO  может быть смотреть количестов просмотров
    # TODO  как оставляется комментарий?
    # TODO  где хранятся картинки

    """Формат ответ [
        { post_id:..., 
          img:  …, 
          description: … , 
          comments: [{}], 
          views: …, 
          is_liked: …,
          is_favorite,
          user: {img: …, name: …, location: ...}
        }
    ]
    """

""" ЛАЙКИ """


@app.route("/posts/<int:postid>/like/")
def post_like():
    """Реализовать лайк """
    # TODO  как мы храним лайкнутость и избранность


@app.route("/posts/<int:postid>/dislike/")
def post_displke():
    """Реализовать  отмену лайка"""
    # TODO  как мы храним лайкнутость и избранность


""" КОММЕНТЫ """


@app.route("/posts/<int:postid>/comments/", methods=["GET"])
def get_comments():
    """Реализовать отдачу помментов комментария"""

    # TODO: отдать все комменты по посту, если поста нет - отдать []


@app.route("/posts/<int:postid>/comments/", methods=["POST"])
def post_comment():
    """Реализовать написание комментария"""

    # TODO: добавить комментарий с спикску комментариев поста


if __name__ == '__main__':
    app.run(debug=True)
