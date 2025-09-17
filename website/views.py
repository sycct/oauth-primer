from flask import Blueprint, redirect, render_template, session, url_for
from flask_login import current_user, login_required

views = Blueprint("views", __name__)


@views.route("/", methods=["GET"])
def home():
    """
    page displayed when server launches
    """

    return render_template("index.html")


@views.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
    """
    renders the dashbaord page, after user has logged in
    """

    return render_template("dashboard.html", user=current_user)
