from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Sign in')


class SignUpForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    # submit = SubmitField('Sign Up')

class PostForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    body=StringField('body', validators=[DataRequired()])
    submit = SubmitField('Create Post')
