from flask import jsonify

from voteitapp import app, db
from voteitapp.models import Post


@app.route('/api/posts', methods=['GET'])
def get_all_posts():
    posts = db.session.query(Post).all()
    return jsonify(posts=[post.serialize() for post in posts])


@app.route('/api/posts/<post_id>', methods=['GET'])
def get_post(post_id):
    post = db.session.query(Post).filter(Post.id == post_id).one()
    return jsonify(post=post.serialize())
