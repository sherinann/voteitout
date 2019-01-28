from flask import app
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

from voteitapp import db, login


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author')

    def __repr__(self):
        return '<User {' + self.username + '} >'

    def set_password_hash(self, password):
        self.password = generate_password_hash(password)

    def check_password_hash(self, password):
        return check_password_hash(self.password, password)
