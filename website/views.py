from flask import Blueprint, redirect, render_template, session, url_for

views = Blueprint("views", __name__)


@views.route("/", methods=["GET"])
def home():
    if "username" in session:
        return redirect(url_for("dashboard"))
    return render_template("index.html")
