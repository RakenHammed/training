import logging

from flask import Flask

from app.config import Config
from app.controllers import users_controller
from app.logger_setup import LoggerSetup

LoggerSetup()
logger = logging.getLogger()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config())

    if test_config and app.config["TESTING"]:
        raise Exception(
            "You are not using the test database, change the testing value in the .env file"
        )

    with app.app_context():
        from app import database
        from app.repositories import sql_alechemy_user_repository

        database.init_db(app)
    app.register_blueprint(users_controller.bp)
    app.add_url_rule("/", endpoint="index")
    return app
