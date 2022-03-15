from flask import Blueprint, render_template, request

from function_work2 import search_for_posts, get_posts_by_user


#logging.basicConfig(filename="info.log", level=logging.INFO, encoding="UTF-8")
post_find_blueprint = Blueprint('post_find_blueprint', __name__, template_folder='templates')


@post_find_blueprint.route('/search')
def post_find_search():
    s = request.args.get("s", "")
    postes = search_for_posts(s)
    return render_template("search.html", postes=postes)

@post_find_blueprint.route('/user/<name>')
def post_find_user(name):
    postes = get_posts_by_user(name)
    return render_template("user-feed.html", postes=postes)