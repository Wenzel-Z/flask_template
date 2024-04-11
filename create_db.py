from app.extensions import db
from app.models.post import Post
from app.models.question import Question
from app import create_app


def create_tables():
    """
    creates the tables defined in app.models, if the table already exists in the db it
    does nothing to that table
    if you want to update a table (e.g. add a column) you must drop that table with
    >>> db.drop_all()
    and then re-initialize the table
    """
    app = create_app()
    with app.app_context():
        db.create_all()


if __name__ == "__main__":
    create_tables()
