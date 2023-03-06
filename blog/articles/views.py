from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

articles_app = Blueprint("articles_app", __name__)
ARTICLES = {
    1: {
        "name": "first",
        "user_id": 1,
    },
    2: {
        "name": "second",
        "user_id": 1,
    },
    3: {
        "name": "third",
        "user_id": 1,
    },
}


@articles_app.route("/", endpoint="list")
def users_list():
    return render_template("articles/list.html", users=ARTICLES)


@articles_app.route("/<int:article_id>/", endpoint="details")
def user_details(user_id: int):
    try:
        user_name = ARTICLES[user_id]
    except KeyError:
        raise NotFound(f"ARTICLES #{user_id} doesn't exist!")
    return render_template('articles/details.html', user_id=user_id, user_name=user_name)
