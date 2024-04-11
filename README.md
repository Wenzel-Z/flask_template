# Code Template For Larger Flask Apps

***

Template repo for launching larger flask applications. 

# How To Use

***

```
# Clone this repository
$ git clone https://github.com/Wenzel-Z/flask_template

# Go into the repository
$ cd flask_template

# Install dependencies
$ pip install -r requirements.txt

# Export flask app environment variable
$ export FLASK_APP=app.py

# Run flask app in debug mode
$ flask run --debug
```

# Initializing a Database

***

``` 
# Create the database
$ python3 create_db.py

# Add dummy data
$ python3 tests/generate_data/generate_questions.py
$ python3 tests/generate_data/generate_posts.py
```

