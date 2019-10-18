from flask import Flask, session, render_template, redirect, url_for, request

@app.route("/")
def index():
    return "Project 1: TODO"

@app.route("/login", methods=['GET', 'POST'])
def login:
    error= None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Username or Password. Please try again.'
        else:
            return redirect(url_for('home'))
        return render_template('login.html', error=error)
