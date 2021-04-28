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

class ProjectForm(FlaskForm):
	project = StringField('Project', validators = [DataRequired()])
	submit = SubmitField('Add Project')

class TaskForm(FlaskForm):
	task = StringField('Task', validators = [DataRequired()])
	submit = SubmitField('Add Task')

class ChangePasswordForm(FlaskForm):
	old_password = StringField('Current Password', validators=[DataRequired()])
	new_password = StringField('New Password', validators=[DataRequired()])
	new_password_confirm = StringField('New Password Confirm', validators=[DataRequired()])
	submit = SubmitField('Change Password')

class DeleteAccountForm(FlaskForm):
	password = StringField('Current Password', validators=[DataRequired()])
	password_confirm = StringField('Current Password Confirm', validators=[DataRequired()])
	submit = SubmitField('DELETE ACCOUNT FOREVER')
