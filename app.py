from flask import Flask


def create_app():
    app = Flask(__name__)
    from api.api import api_post_all
    app.register_blueprint(api_post_all)

    return app
