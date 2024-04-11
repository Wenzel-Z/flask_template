"""
NOTICE: to update the db you first have to delete the current db,
you do so by running `db.drop_all()` in the shell   

to initialize the db:
1 - open the flask shell
2 - run:
  >>> from app.extensions import db
  >>> from app.models.post import Post
  >>> from app.models.question import Question
  >>> db_create_all()
  >>> exit()

if there are more models than the ones specified above, import those as well
"""
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
