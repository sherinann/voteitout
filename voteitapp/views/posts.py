from datetime import datetime

from flask import render_template, request
from flask_login import current_user
from werkzeug.utils import redirect

from voteitapp import app, db
from voteitapp.models import Post
from voteitapp.forms import PostForm


@app.route('/post/create', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    if request.method == 'POST':
        user_id = current_user.id
        post = Post(title=form.data['title'], body=form.data['body'], timestamp=datetime.utcnow(),
                    user_id=user_id)
        db.session.add(post)
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('/post/create.html', title='create post', form=form)


@app.route('/')
@app.route('/posts')
def posts():
    posts = db.session.query(Post).all()
    return render_template('post/posts.html', posts=posts)


@app.route('/post/<id>/', methods=['POST', 'GET'])
def post_detail(id):
    post = db.session.query(Post).filter(Post.id == id).one()
    if request.method == 'GET':
        return render_template('post/detail.html', post=post)
    else:
        vote = int(request.values['votes'])
        if vote == -1:
            post.downvotes = post.downvotes + 1
        if vote == 1:
            post.upvotes = post.upvotes + 1
        db.session.commit()
        return render_template('post/detail.html', post=post)


@app.route('/posts/<id>/', methods=['GET'])
def get_posts(id):
    posts = db.session.query(Post).filter(Post.user_id == id).all()
    return render_template('post/posts.html', posts=posts)


@app.route('/myposts', methods=['GET'])
def get_current_user_posts():
    posts = db.session.query(Post).filter(Post.user_id == current_user.id).all()
    if posts:
        return render_template('post/posts.html', posts=posts)
    else:
        return redirect('/')

#
# @app.route('/search/<topic>/', methods=['GET'])
# def search_posts(topic):
#     posts = db.session.query(Post).filter(Post.title == topic).all()
#     if posts:
#         return render_template('post/posts.html', posts=posts)
#     else:
#         return redirect('/')
