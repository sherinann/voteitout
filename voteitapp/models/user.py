from flask import app
from sqlalchemy import Table
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

from voteitapp import db, login

Base = declarative_base()


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


association_table = Table('association', Base.metadata,
                          db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                          db.Column('topic_id', db.Integer, db.ForeignKey('topic.id')),
                          )


class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author')
    topics = db.reationship('Topic', secondary=association_table)

    def __repr__(self):
        return '<User {' + self.username + '} >'

    def set_password_hash(self, password):
        self.password = generate_password_hash(password)

    def check_password_hash(self, password):
        return check_password_hash(self.password, password)
