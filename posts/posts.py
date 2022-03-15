from flask import Blueprint, render_template

from function_work2 import get_posts_all, get_comments_by_post_id, get_post_by_pk

post_all_blueprint = Blueprint('post_all_blueprint', __name__, template_folder='templates')


@post_all_blueprint.route('/')
def post_all():
    postes = get_posts_all()
    return render_template("index.html", postes=postes)


@post_all_blueprint.route('/posts/<postid>')
def post_id(postid):
    post = get_post_by_pk(postid)
    comments = get_comments_by_post_id(postid)
    return render_template("post.html", post=post, comments=comments)
