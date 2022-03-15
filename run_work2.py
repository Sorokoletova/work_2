from flask import Flask
from posts.posts import post_all_blueprint
from post_find.post_find import post_find_blueprint

app = Flask(__name__)

app.register_blueprint(post_all_blueprint)
app.register_blueprint(post_find_blueprint)

app.run()
