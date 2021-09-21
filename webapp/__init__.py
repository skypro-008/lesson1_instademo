from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import ProductionConfig

app = Flask(__name__)
app.config.from_object(ProductionConfig)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
