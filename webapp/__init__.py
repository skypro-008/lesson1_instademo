from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ('postgres://azzyswikpgmtfu:' +
                                         '9c2f4c36cdc270cba8cdb00f51' +
                                         'a1e5dd5acba094fcd9898878f6' +
                                         '979ce848eca0@ec2-54-158-247' +
                                         '-97.compute-1.amazonaws.com:' +
                                         '5432/d951cg60mur8eo')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
