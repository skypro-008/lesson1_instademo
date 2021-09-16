from webapp import app, db
from webapp import models, views    # noqa F401


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Post': models.Post, 'Comment': models.Comment}
