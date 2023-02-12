from flask import Blueprint, request

from app.entities.credentials import Credentials
from app.entities.user import User
from app.entities.user_filters import UserFilters
from app.errors.sql_database_errors import SqlDatabaseError
from app.errors.user_errors import EmailAlreadyExistsError, UserIdDoesNotExists
from app.services.user_services import (
    EmailNotFoundError,
    PasswordDoesNotMatchError,
    UserServices,
)

bp = Blueprint("users_controller", __name__, url_prefix="/users")


@bp.route("/<int:_id>", methods=["GET"])
def get_one(_id):
    try:
        user = UserServices().get_one_by(_id)
        response = {"user": user}
        return response, 200
    except SqlDatabaseError as error:
        return str(error), 500


@bp.route("/", methods=["GET"])
def get_all():
    filters = request.json
    try:
        users = UserServices().get_all_by(UserFilters(**filters))
        response = {"users": users}
        return response, 200
    except SqlDatabaseError as error:
        return str(error), 500


@bp.route("/", methods=["POST"])
def create():
    user_params = request.json
    try:
        user = UserServices().create(User(**user_params))
        response = {"user": user}
        return response, 200
    except EmailAlreadyExistsError as error:
        return str(error), 409
    except SqlDatabaseError as error:
        return str(error), 500


@bp.route("/auth", methods=["POST"])
def login():
    credentials_params = request.json
    credentials = Credentials(**credentials_params)
    try:
        user = UserServices().get_user_if_valid(credentials)
        response = {"user": user}
        return response, 200
    except EmailNotFoundError as error:
        return str(error), 401
    except PasswordDoesNotMatchError as error:
        return str(error), 401


@bp.route("/<int:_id>", methods=["PATCH"])
def update(_id):
    user_params = request.json
    try:
        user = UserServices().update(_id, User(**user_params))
        response = {"user": user}
        return response, 200
    except UserIdDoesNotExists as error:
        return str(error), 404
    except SqlDatabaseError as error:
        return str(error), 500


@bp.route("/<int:_id>", methods=["DELETE"])
def delete(_id):
    try:
        UserServices().delete(_id)
        response = {}
        return response, 200
    except UserIdDoesNotExists as error:
        return str(error), 404
    except SqlDatabaseError as error:
        return str(error), 500
