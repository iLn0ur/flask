from flask import Flask, render_template, request

from blog.admin import admin
from blog.articles.views import articles_app
from blog.auth.views import auth_app, login_manager
from blog.models.database import db
from blog.security import flask_bcrypt
from blog.users.views import users_app
import os
from blog.authors.views import authors_app
from blog.api import init_api


app = Flask(__name__)
cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
app.config.from_object(f"blog.configs.{cfg_name}")
api = init_api(app)


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

app.register_blueprint(authors_app, url_prefix="/authors")


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


@app.cli.command("create-tags")
def create_tags():
    """
    Run in your terminal:
    ➜ flask create-tags
    """
    from blog.models import Tag
    for name in [
        "flask",
        "django",
        "python",
        "sqlalchemy",
        "news",
    ]:
        tag = Tag(name=name)
        db.session.add(tag)
    db.session.commit()
    print("created tags")


admin.init_app(app)
