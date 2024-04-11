from app.models.post import Post


def test_posts_get_index(client):
    response = client.get("/posts/")
    assert b'This is the posts Flask blueprint' in response.data
    # ensure database was accessed successfully
    assert b'Post #430' in response.data


def test_posts_get_categories(client):
    response = client.get("/posts/categories/")
    assert b'This is the categories page within the posts blueprint' in response.data


def test_posts_database(client, app):
    with app.app_context():
        assert Post.query.count() == 1
        assert Post.query.first().title == "Post #430"
