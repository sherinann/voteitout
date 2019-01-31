from flask import jsonify

from voteitapp import app, db
from voteitapp.models import Topic


@app.route('/api/topics', methods=['GET'])
def get_all_topics():
    topics = db.session.query(Topic).all()
    return jsonify(topics=[topic.serialize() for topic in topics])
