from datetime import datetime

from voteitapp import db


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    post = db.Column(db.Integer, db.ForeignKey('post.id'))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def serialize(self):
        return {
            'id':self.id,
            'body':self.body,
            'post':self.post,
            'timestamp':self.timestamp,
            'user_id':self.user_id
        }