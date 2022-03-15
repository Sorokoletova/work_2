from flask import Flask
import pytest
from app import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


@pytest.fixture()
def keys_post():
    return ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']
