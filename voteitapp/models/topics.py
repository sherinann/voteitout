from voteitapp import db


class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    posts = db.relationship('Post', backref='topic')
