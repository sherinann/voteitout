from flask import jsonify

from voteitapp import app, db
from voteitapp.models import Comment


@app.route('/api/comments', methods=['GET'])
def get_all_comments():
    comments = db.session.query(Comment).all()
    return jsonify(comments=[comment.serialize() for comment in comments])
