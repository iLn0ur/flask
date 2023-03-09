from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Boolean, LargeBinary
from blog.models.database import db
from blog.security import flask_bcrypt


class User(db.Model, UserMixin):
    _password = Column(LargeBinary, nullable=True)

    id = Column(Integer, primary_key=True)
    first_name = Column(String(120), unique=False, nullable=False, default="", server_default="")
    last_name = Column(String(120), unique=False, nullable=False, default="", server_default="")
    email = Column(String(255), unique=True, nullable=False, default="", server_default="")
    is_staff = Column(Boolean, nullable=False, default=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = flask_bcrypt.generate_password_hash(value)

    def validate_password(self, password) -> bool:
        return flask_bcrypt.check_password_hash(self._password, password)

    def __repr__(self):
        return f"<User #{self.id} {self.username!r}>"
