from app.models.question import Question


def test_new_question(client, app):
    client.post("/questions/", data={"content": "this is a test question",
                                     "answer": "this is a test answer"})

    with app.app_context():
        assert Question.query.count() == 1
        assert Question.query.first().content == "this is a test question"


