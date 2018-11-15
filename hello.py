from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)


@app.route("/")
def index():
    return "Index!"


@app.route("/hello")
def hello():
    return "Hello World!"


@app.route("/members")
def members():
    return "Members"


@app.route("/members/<string:name>/")
def getmembers(name):
    return render_template('index.html', name=name)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)