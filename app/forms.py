"""module to create login form class with fields"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """class LoginForm is used to supply the login.html the appropriate data, it contains all the fields required for
    viewing on the html"""

    username = StringField('Username', validators=[DataRequired()])         # declaring the username field (String)
    password = PasswordField('Password', validators=[DataRequired()])       # declaring the password field (Password)
    remember_me = BooleanField('Remember Me')                               # declaring the remember me field (Bool)
    submit = SubmitField('Sign In')                                         # declaring the submit button
