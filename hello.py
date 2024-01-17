"""
cicd-test-api
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    """
    hello world api
    """
    return "<p>the Fuck! Python env! Fuck the virtual! Jesus!</p>"

@app.route("/index")
def index():
    """
    index api
    """
    branch_condition = 1
    if branch_condition == 1:
        return "<p>index</p>"
    return f"<p>index {branch_condition}</p>"
