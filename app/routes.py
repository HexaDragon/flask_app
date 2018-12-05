"""different urls to route to"""

from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    """return the homepage"""
    user = {'username': 'H3xDrgn'}      # creating dictionary obj to store mock users
    return render_template('index.html', title='Home',
                           user=user)
