from flask import Flask, request
app = Flask(__main__)

""" ПОСТЫ """

@app.route("/posts/")
def get_posts():

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






app.run()













