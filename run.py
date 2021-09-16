from webapp import app, cli, db, models, views  # noqa F401

cli.register_posts(app)
cli.register_comments(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Post': models.Post, 'Comment': models.Comment}
