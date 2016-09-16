#!usr/bin/python

from app import app, db
from flask import render_template, redirect, request, url_for
from models import User


@app.route('/')
def index():
    return render_template('add_user.html')


@app.route('/post_user', methods=['POST', 'GET'])
def post_user():
    user = User(request.form['username'], request.form['email'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))
