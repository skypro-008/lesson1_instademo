from pprint import pprint

import click

from webapp.models import Comment, Post


def register_posts(app):
    @app.cli.group()
    def posts():
        """ Добавление/просмотр/редактирование постов. """
        pass

    @posts.command()
    @click.argument('post_id', type=int, default=0)
    def show(post_id):
        """ Показать все или посты или `post_id`. """
        if not post_id:
            print([
                post.to_dict()
                for post in Post.query.all()
            ])
        else:
            post = Post.query.filter_by(id=post_id).first()
            if post:
                pprint(post.to_dict())
            else:
                print('Нет такого поста')

    @posts.command()
    @click.argument('post_id', type=int, default=0)
    def delete(post_id):
        """ Удалить один или несколько постов. """
        if post_id:
            post = Post.query.filter_by(id=post_id).first()
            if not post:
                print('Такого поста нет')
            elif input(f'Хочешь удалить пост #{post_id}? [Y/n] ').lower() == 'y':
                Post.query.filter_by(id=post_id).delete()
        else:
            if input('Хочешь удалить все посты? [Y/n] ').lower() == 'y':
                for post in Post.query.all():
                    post.delete()

    @posts.command()
    @click.argument('post_id', type=int)
    def clear(post_id):
        """ Удалить все комментарии к посту """
        post = Post.query.filter_by(id=post_id).first()
        if post:
            comments = post.comments
            if input(f'Хочешь удалить все комментарии? ({len(comments)}) [Y/n] ').lower() == 'y':
                for comment in comments:
                    comment.delete()
        else:
            print('Нет такого поста')

    @posts.command()
    def create():
        """ Создаем пост. """
        author = input('Автор: ')
        content = input('Контент: ')
        image = input('Картинка: ')
        post = Post(author, content, image)
        if input('Создаем? [Y/n] ').lower() == 'y':
            post.add()
            return pprint(post.to_dict())


def register_comments(app):
    @app.cli.group()
    def comments():
        """ Добавление/просмотр/редактирование комментариев. """
        pass

    @comments.command()
    @click.argument('comment_id', type=int)
    def show(comment_id):
        """ Показывает определенный комментарий"""
        comment = Comment.query.filter_by(id=comment_id).first()
        if comment:
            pprint(comment.to_dict())
        else:
            print('Нет такого комментария')

    @comments.command()
    @click.argument('comment_id', type=int)
    def delete(comment_id):
        if comment_id:
            if input(f'Хочешь удалить комментарий #{comment_id}? [Y/n] ').lower() == 'y':
                Comment.query.filter_by(id=comment_id).delete()

    @comments.command()
    @click.argument('post_id', type=int)
    def create(post_id):
        post = Post.query.filter_by(id=post_id).first()
        if post:
            author = input('Автор: ')
            content = input('Контент: ')
            comment = Comment(author, content, post.id)
            if input('Создаем? [Y/n] ').lower() == 'y':
                comment.add()
                return pprint(comment.to_dict())
        else:
            print('Нет такого поста')
