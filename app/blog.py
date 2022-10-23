from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from app.auth import login_required

bp = Blueprint("blog", __name__)


@bp.route("/")
def index():
    pass


@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    pass


@bp.route("/<int:id>/update", methods=("GET", "POST"))
@login_required
def update(id):
    pass


@bp.route("/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    pass


def get_post(id, check_author=True):
    pass
