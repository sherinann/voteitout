from voteitapp import db
from voteitapp.models.post import post_topic_association_table


class Topic(db.Model):

    __tablename__ = 'topic'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    posts = db.relationship('Post', secondary=post_topic_association_table, back_populates='topics')

    def __repr__(self):
        return '<topic + {' + self.name + '} >'


