import pytest

from app import create_app
from app.extensions import db
from app.models.post import Post
from config import TestConfig


@pytest.fixture()
def app():
    app = create_app(config_class=TestConfig)
    with app.app_context():
        # create db
        db.create_all()

        # add a post to the post table for later testing
        post = Post(title=f'Post #430',
                    content=f'Content #1000')
        db.session.add(post)
        db.session.commit()

    yield app

    # teardown goes here...


@pytest.fixture()
def client(app):
    return app.test_client()
