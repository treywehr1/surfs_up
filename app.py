# Import flask dependency
from flask import Flask

# Create a new instance/Flask app
app = Flask(__name__)

# Create a root Flask route
@app.route('/')

def hello_world():
    return 'Hello World'