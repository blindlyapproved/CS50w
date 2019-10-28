import os

from flask import Flask, flash, request, session, redirect, render_template, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from passlib.hash import pbkdf2_sha256

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

# Standard route for the app aka home
@app.route("/")
def index():
    return render_template("index.html")

# Route  to register an account, with double pw check
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        if session.get("logged_in"):
            flash("You are already logged in.")
            return redirect(url_for('index'), "303")
        else:
            return render_template("register.html")
        if request.method == "POST":
            username = request.form.get("username")
            pw1 = request.form.get('password')
            pw2 = request.form.get('pw2')

#            if pw1 != pw2 or pw1 is None or pw2 is None
#            flash("The passwords do not match")
#            return redirect(url_for('register'), "303")

        hash = pbkdf2_sha256.hash(pass1)
        db.execute("INSERT INTO users (username, password) VALUES (:name, :hash)",
                    {"name": username, "hash": hash})
        db.commit()
        flash("You successfully created your Boocklub account")
        return redirdct(url_for('register'), "303")


# Route to login to an account
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
            if session.get("logged_in"):
                flash("You are already logged in.")
                return redirect(url_for('index'), "303")
    else:
        return render_template("login.html")
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        res = db.execute("SELECT id, password FROM users WHERE username LIKE :name", {"name": username}).fetchone()
        db_hash = res.password
        user_id = res.id

        if not res:
            flash("This user does not exist.")
            return redirect(url_for('login'), "303")

    # db_hash = db_hash[0].encode("utf-8")
    if pbkdf2_sha256.verify(password, db_hash):
        session["logged_in"] = True
        session["user_id"] = user_id
        session["username"] = username
        flash("You successfully logged in.")
        return redirect(url_for('index'), "303")

    else:
        flash("Invalid credentials.")
        return redirect(url_for('login'), "303")

@app.route('/logout')
def logout():
    session["logged_in"] = False
    session["user_id"] = None
    flash("Logout successful.")
    return redirect(url_for('index'))


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
