from datetime import datetime

from flask import request
from flask_login import current_user

from voteitapp import app, Comment, db
from voteitapp.forms import CommentForm


@app.route('/comment/add/<post.id>/', methods=['GET', 'POST'])
def add_comment(post_id):
    form = CommentForm()
    if request.method == 'POST':
        comment = Comment(body=form.data['body'], post=post_id, timestamp=datetime.utcnow(),
                          user_id=current_user.id)
        db.session.add(comment)
        db.session.commit()


def get_comments(post_id):
    comments = db.session.query(Comment).filter(Comment.post == post_id).all()
