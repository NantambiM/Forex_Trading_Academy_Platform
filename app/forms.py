from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from . models import Quiz, Question, User


class RegisterForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(), Length(min=3, max=20)]
    )

    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=6)]
    )

    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired()]
    )

    submit = SubmitField("Login")


class UpdateProfileForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(), Length(min=3, max=20)]
    )

    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )

    submit = SubmitField("Save Changes")


class ChangePasswordForm(FlaskForm):
    current_password = PasswordField(
        "Current Password",
        validators=[DataRequired()]
    )

    new_password = PasswordField(
        "New Password",
        validators=[DataRequired(), Length(min=6)]
    )

    confirm_password = PasswordField(
        "Confirm New Password",
        validators=[DataRequired(), EqualTo('new_password', message='Passwords must match.')]
    )

    submit = SubmitField("Update Password")