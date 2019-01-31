from datetime import datetime

from flask import request, render_template
from flask_login import current_user
from werkzeug.utils import redirect

from voteitapp import app, db
from voteitapp.models import Comment
from voteitapp.forms import CommentForm



@app.route('/comments/comment/<post_id>', methods=['GET', 'POST'])
def add_comment(post_id):
    form = CommentForm()
    if request.method == 'POST':
        comment = Comment(body=form.data['body'], post=post_id, timestamp=datetime.utcnow(),
                          user_id=current_user.id)
        db.session.add(comment)
        db.session.commit()

        return redirect('posts/post/'+post_id)
    else:
        return render_template('comments/comment.html', form=form, post_id=post_id)


def get_comments(post_id):
    comments = db.session.query(Comment).filter(Comment.post == post_id).all()
