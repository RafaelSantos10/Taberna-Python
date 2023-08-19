from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField, \
    TextAreaField, StringField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField("email", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")


class CreateNewPost(FlaskForm):
    title = StringField("title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])


class UpdatePost(FlaskForm):
    title = StringField("title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])


class CreateNewUser(FlaskForm):
    email = EmailField("email", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    name = StringField("email", validators=[DataRequired()])
    user_name = StringField("password", validators=[DataRequired()])
