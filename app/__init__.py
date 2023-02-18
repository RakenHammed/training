from flask import Flask

from app.config import config
from app.logger import logger


def create_app(test_config: dict = None):
    logger.info("Logger is setup")
    app = Flask(__name__, instance_relative_config=True)

    if not test_config:
        app.config.from_object(config)
    else:
        app.config.from_mapping(test_config)
    with app.app_context():
        from app import database
        from app.repositories import sql_alechemy_user_repository

        database.init_db(app)
    from app.controllers import users_controller

    app.register_blueprint(users_controller.bp)
    app.add_url_rule("/", endpoint="index")
    return app
