def test_app_get_index(client):
    response = client.get('/')
    assert b"<title> Home Page of Flask Template </title>" in response.data


