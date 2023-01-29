from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, HiddenField, SubmitField


class LoginForm(FlaskForm):
    email = StringField('Email Address', [validators.Length(min=6, max=30)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.Length(min=8, max=30)
    ])
    submit = SubmitField(label="Log In")
    csrf_token = HiddenField()
