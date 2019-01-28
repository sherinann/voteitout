from datetime import datetime

from sqlalchemy import Table

from voteitapp import db

post_topic_association_table = Table('post_topic_association', db.metadata,
                                     db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True),
                                     db.Column('topic_id', db.Integer, db.ForeignKey('topic.id'), primary_key=True))


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.String(1000))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    upvotes = db.Column(db.Integer, default=0)
    downvotes = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    topics = db.relationship('Topic', secondary=post_topic_association_table, back_populates='posts')

    def __repr__(self):
        return '<Post {' + self.body + '} >'
