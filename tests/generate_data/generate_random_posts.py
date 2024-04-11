import random

from app.extensions import db
from app.models.post import Post
from app import create_app


def generate_posts():
    """
    generates 10 random posts to test db functionality
    """
    app = create_app()
    with app.app_context():
        for i in range(0, 10):
            random_num = random.randrange(1, 1000)
            post = Post(title=f'Post #{random_num}',
                        content=f'Content #{random_num}')
            db.session.add(post)
            print(post)
            print(post.content)
            print('--')
            db.session.commit()


if __name__ == "__main__":
    generate_posts()
