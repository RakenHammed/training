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
    if (
        test_config
        and not app.config.get("TESTING")
        or not test_config
        and app.config.get("TESTING")
    ):
        raise Exception(f"You are not using the right database {Config()}")
    with app.app_context():
        from app import database
        from app.repositories import sql_alechemy_user_repository

        database.init_db(app)
    app.register_blueprint(users_controller.bp)
    app.add_url_rule("/", endpoint="index")
    return app
