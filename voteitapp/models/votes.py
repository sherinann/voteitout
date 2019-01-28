from voteitapp import db


class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    post = db.Column(db.Integer, db.ForeignKey('post.id'))
    vote = db.Column(db.Integer)