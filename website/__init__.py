from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    """
        create the main application
    """
    app = Flask(__name__)
    app.config["SECRET_KEY"]= os.environ.get("SECRET_KEY")

    # import & register various blueprints
    from .auth import auth
    app.register_blueprint(auth, url_prefix="/auth/")
    from .views import views
    app.register_blueprint(views, url_prefix="/")
    # from .oauth import oauth
    # app.register_blueprint(oauth, url_prefix="/oauth/")
    # from .models import models

    return app
