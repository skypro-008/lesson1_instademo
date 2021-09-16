from webapp import db


class SQLMixin:

    def add(self):
        db.session.add(self)
        db.session.commit()
        return self

    def save(self):
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
