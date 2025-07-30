from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/hello_world")
def hello_world():
    return "<p>Hello, World!</p>"