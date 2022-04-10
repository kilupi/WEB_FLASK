from app import app
from flask import render_template, url_for


@app.route('/')
@app.route('/hello')
def hello():
    return render_template('Index.html')


@app.route('/users2/<username>')
def users2(username):
    return 'User %s' % username


@app.route('/users/<username>')
def users(username):
    return render_template('Index 1.html')
