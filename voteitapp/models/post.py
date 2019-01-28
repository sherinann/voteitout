from datetime import datetime

from voteitapp import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.String(1000))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    upvotes = db.Column(db.Integer, default=0)
    downvotes = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    topic = db.Column(db.Integer, db.ForeignKey('topic.id'))
    comments = db.relationship('Comments', backref='post')


    def __repr__(self):
        return '<Post {' + self.body + '} >'
