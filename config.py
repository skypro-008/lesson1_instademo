import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://{login}:{password}@{host}:5432/{schema}'.format(
        login=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS'),
        host='ec2-54-158-247-97.compute-1.amazonaws.com',
        schema='d951cg60mur8eo'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
