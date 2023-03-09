from flask import Flask, render_template, request

from blog.articles.views import articles_app
from blog.auth.views import auth_app, login_manager
from blog.models.database import db
from blog.security import flask_bcrypt
from blog.users.views import users_app
import os


app = Flask(__name__)
cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
app.config.from_object(f"blog.configs.{cfg_name}")


# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/blog.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#
# app.config["SECRET_KEY"] = "abcdefg123456"

login_manager.init_app(app)
flask_bcrypt.init_app(app)
db.init_app(app)
app.register_blueprint(auth_app, url_prefix="/auth")
app.register_blueprint(users_app, url_prefix="/users")

app.register_blueprint(articles_app, url_prefix="/articles")


@app.route("/")
def index():
    return render_template("users/list.html")


@app.route("/greet/<name>/")
def greet_name(name: str):
    return f"Hello {name}!"

"""
> http://127.0.0.1:5000/user/
- User [no name] [no surname]
> http://127.0.0.1:5000/user/?name=John&surname=Smith
- User John Smith
"""

@app.route("/user/")
def read_user():
    name = request.args.get("name")
    surname = request.args.get("surname")
    return f"User {name or '[unknown]'} {surname or '[unknown]'}"
