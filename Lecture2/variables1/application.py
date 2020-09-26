import random

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = random.choice(["Hello, world!", "Hi there!", "Good morning!"])
    return render_template("index.html", headline=headline)

@app.route("/bye")
def bye():
    headline = random.choice(["Hello, world!", "Bye there!", "See ya!"])
    return render_template("index.html", headline=headline)
