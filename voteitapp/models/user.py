from flask import app
from sqlalchemy import Table
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from topics import Topic
from voteitapp import db, login




@login.user_loader
def load_user(id):
    return User.query.get(int(id))


user_topic_association_table = Table('association', db.metadata,
                          db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                          db.Column('topic_id', db.Integer, db.ForeignKey('topic.id'),  primary_key=True)
                          )


class User(UserMixin, db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author')
    topics = db.relationship('Topic', secondary=user_topic_association_table)

    def __repr__(self):
        return '<User {' + self.username + '} >'

    def set_password_hash(self, password):
        self.password = generate_password_hash(password)

    def check_password_hash(self, password):
        return check_password_hash(self.password, password)



