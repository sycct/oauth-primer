from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager
import os
from dotenv import load_dotenv

load_dotenv()
db = SQLAlchemy()
db_name = "oauth.db"


def create_app():
    """
    create the main application
    """
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_name}"
    # allow each user to have a unique db
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # import & register various blueprints
    from .auth import auth

    app.register_blueprint(auth, url_prefix="/auth/")
    from .views import views

    app.register_blueprint(views, url_prefix="/")
    # from .oauth import oauth
    # app.register_blueprint(oauth, url_prefix="/oauth/")
    from .models import User

    create_database(app)

    # implement flask_login functionality
    login_manager = LoginManager()
    login_manager.init_app(app)
    # when users try to access a login_required view without being
    # logged in, theyre redirected here
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Oh no! You need to be logged in to access this page"
    login_manager.login_message_category = "warning"

    @login_manager.user_loader
    def load_user(user_id):
        """
        check if use exists in db.
        takes in user_id string and returns corresponding user object.
        else none is returned
        """
        return User.query.get(user_id)

    return app


def create_database(app):
    """
    create the sqlite db
    """
    with app.app_context():
        if not os.path.exists("website" + db_name):
            db.create_all()
            print("The database has been created successfully!")
        else:
            print("An error occurred while creating the database!")
