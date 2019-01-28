from flask import render_template

from voteitapp import app, db, Post


@app.route('/posts/<topic>')
def get_posts(topic):
    posts = db.session.query(Post).filter(topic == topic).all(0)
    return render_template('post/posts.html', posts=posts)


