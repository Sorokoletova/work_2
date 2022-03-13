from flask import Flask, send_from_directory
from posts.posts import post_all_blueprint

app = Flask(__name__)

app.register_blueprint(post_all_blueprint)


app.run()
