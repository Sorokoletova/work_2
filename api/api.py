from flask import Blueprint, jsonify

from function_work2 import get_posts_all, get_post_by_pk

api_post_all = Blueprint('api_post_all', __name__)


@api_post_all.route('/api/posts')
def post_all():
    postes = get_posts_all()
    return jsonify(postes)


@api_post_all.route('/api/posts/<int:post_id>')
def post_all_id(post_id):
    postes = get_post_by_pk(post_id)
    return jsonify(postes)
