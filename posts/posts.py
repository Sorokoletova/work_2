from flask import Blueprint, render_template, request

from function_work2 import get_posts_all, get_comments_by_post_id, get_post_by_pk


#logging.basicConfig(filename="info.log", level=logging.INFO, encoding="UTF-8")
post_all_blueprint = Blueprint('post_all_blueprint', __name__, template_folder='templates')


@post_all_blueprint.route('/')
def post_all():
    postes = get_posts_all()
    return render_template("index.html", postes=postes)


@post_all_blueprint.route('/posts/<postid>')
def post_id():
    postid = request.args.get("pk")
    postes = get_post_by_pk(postid)
    comments = get_comments_by_post_id(postid)
    return render_template("post.html", post=postes, comment=comments)