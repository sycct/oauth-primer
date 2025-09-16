from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET"])
def login():
    return render_template("index.html")
