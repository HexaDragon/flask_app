"""different urls to route to"""

from app import app


@app.route('/')
@app.route('/index')
def index():
    """return the message string"""
    return "Hello H3xDrgn..."
