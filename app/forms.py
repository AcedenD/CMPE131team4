from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class TaskForm(FlaskForm):
	task = StringField('Task', validators = [DataRequired()])
	submit = SubmitField('Add Task')

class TimeForm(FlaskForm):
	clock_in = SubmitField('Clock In')
	clock_out = SubmitField('Clock Out')
	past_hours = SubmitField('Check Hours Worked')
