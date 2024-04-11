from app.extensions import db
from app.models.question import Question
from app import create_app


def generate_questions():
    """
    generates 10 random posts to test db functionality
    """
    app = create_app()
    with app.app_context():
        question_1 = Question(content="This is a test", answer="This is the answer")
        question_2 = Question(content="This is a second test", answer="This is the second answer")
        db.session.add(question_1)
        db.session.add(question_2)
        db.session.commit()


if __name__ == "__main__":
    generate_questions()
