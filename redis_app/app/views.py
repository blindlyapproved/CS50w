from app import app
from app.tasks import count_words
from app import q

from flask import render_template, request

from time import strftime

@app.route("/index")
def index():
    return "Hello Luuk"

@app.route("/add-task", method=["GET", "POST"])
def add_task():

