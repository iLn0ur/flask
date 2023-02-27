from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello web!"


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
