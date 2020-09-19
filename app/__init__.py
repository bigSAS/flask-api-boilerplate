import logging

from flask import Flask, request
from flask_migrate import Migrate
from flask_cors import CORS


from app.config import Config
from app.blueprints.hello import hello_blueprint
# from app.db.schema import db, bcrypt, UserGroup
# from cusg.utils.http import ValidationError, error_response  # todo: new http utlis


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=False)
    # todo: setup loggers
    CORS(app, resources=r'/api/*')
    conf = Config  # todo: env based config
    app.config.from_object(conf)
    # todo: base db
    # db.init_app(app)
    # mirgate = Migrate()
    # mirgate.init_app(app, db)
    # bcrypt.init_app(app)
    # jwt.init_app(app)  # todo: jwt
    app.register_blueprint(hello_blueprint, url_prefix='/hello')
    # app.register_error_handler(Exception, error_response)  # todo: generic error handler from http utils
    return app
