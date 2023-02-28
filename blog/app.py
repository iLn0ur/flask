from flask import Flask, render_template, request

from blog.articles.views import articles_app
from blog.users.views import users_app

app = Flask(__name__)
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
