from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/luuk")
def luuk():
    return render_template("luuk.html")
