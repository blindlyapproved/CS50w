import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    sashie_birthday = now.month == 9 and now.day == 22
    return render_template("index.html", sashie_birthday=sashie_birthday)
