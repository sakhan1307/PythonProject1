from flask import Flask
from test1 import add_two

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/members")
def members():
    return "Members"


@app.route("/members/<string:name>/")
def getmember(name):
    return name


@app.route("/add/<int:a>/<int:b>/")
def get_add(a, b):
    x = add_two(3, 5)
    print(x)
    return str(x)


if __name__ == '__main__':
    app.run()
