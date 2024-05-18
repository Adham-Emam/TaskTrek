from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models import User


class RegistrationForm(FlaskForm):
    username = StringField(validators=[DataRequired(), Length(
        min=2, max=20)], render_kw={"placeholder": "Username"})
    email = StringField(validators=[DataRequired(), Email()], render_kw={
                        "placeholder": "Email"})
    password = PasswordField(validators=[DataRequired()], render_kw={
                             "placeholder": "Password"})
    confirm_password = PasswordField(validators=[DataRequired(), EqualTo(
        'password')], render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'That email is already in use. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField(validators=[DataRequired(), Email()], render_kw={
                        "placeholder": "Email"})
    password = PasswordField(validators=[DataRequired()], render_kw={
                             "placeholder": "Password"})
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()], render_kw={
                        'placeholder': 'Task Title'})

    description = StringField('Description', render_kw={
                              'placeholder': 'Task Description'})

    completed = BooleanField('Completed', render_kw={'placeholder': 'Task completion'})

    submit = SubmitField('Submit')
