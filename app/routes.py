"""different urls to route to"""
import time

from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    """return the homepage"""
    user = {'username': 'H3xDrgn'}      # creating dictionary obj to store mock users
    posts = [
        {
            'author': {'username': 'Rohan', 'date': time.ctime()},
            'body': r"Awesome India and it's raising"
        },
        {
            'author': {'username': 'Shubham', 'date': time.ctime()},
            'body': r"Company Laws and Accounts"
        }
    ]
    return render_template('index.html', title='Home',
                           user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
