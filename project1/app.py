import os

from flask import Flask, session, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL")=="postgres://spfjxchcicutmo:993c2a795902efebcbd301004fbfd4e089c839dcf4113162aaec4b6f6fece33c@ec2-54-246-100-246.eu-west-1.compute.amazonaws.com:5432/dbh7invlfb8eg3":
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine('postgres://spfjxchcicutmo:993c2a795902efebcbd301004fbfd4e089c839dcf4113162aaec4b6f6fece33c@ec2-54-246-100-246.eu-west-1.compute.amazonaws.com:5432/dbh7invlfb8eg3')
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'luuk' or request.form['password'] != 'luuk':
            error = 'Wrong username or password.'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
