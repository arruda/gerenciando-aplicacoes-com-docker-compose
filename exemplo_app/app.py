# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os


class Config(object):
    DEVELOPMENT = True
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'

    def get_db_config():
        db_user = os.environ['DB_ENV_POSTGRES_USER']
        db_pass = os.environ['DB_ENV_POSTGRES_PASSWORD']
        db_name = os.environ['DB_ENV_POSTGRES_USER']
        db_address = os.environ['DB_PORT_5432_TCP_ADDR']
        db_port = os.environ['DB_PORT_5432_TCP_PORT']
        db_url = "postgresql://{user}:{passwd}@{address}:{port}/{name}"
        return db_url.format(
                user=db_user,
                passwd=db_pass,
                address=db_address,
                port=db_port,
                name=db_name
            )

    SQLALCHEMY_DATABASE_URI = get_db_config()


app = Flask(__name__)
app.config.from_object('app.Config')
db = SQLAlchemy(app)


from models import Pessoa


@app.route('/')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
