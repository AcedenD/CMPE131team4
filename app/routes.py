from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
import uuid

from app import myapp_obj
from app import db
from app.forms import LoginForm, RegisForm, TaskForm, ProjectForm

from app.models import User, Tasks, Project


@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect("/home") 
	form = LoginForm()
	if form.validate_on_submit():
        # User.query.filter_by() returns a list from the User table
        # first() returns first element of the list
        # the form.username.data is getting the info the user submitted in the form
		user = User.query.filter_by(username=form.username.data).first()
		print(form.username.data)
        # if no user found or password for user incorrect
        # user.check_password() is a method in the User class
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect('/login')
        # let flask_login library know what user logged int
        # it also means that their password was correct
		login_user(user, remember=form.remember_me.data)

        # return to page before user got asked to login
        # for example, if user tried to access a wedpage called profile, but since they
        # weren't logged in they would get redirected to login page. After they log in
        # the user will be redirected to their previous request, which would be the profile
        # page in this case.
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			# project is a home page
			next_page = url_for('home')

		return redirect(next_page)

	return render_template('login.html', title='Sign In', form=form)


@myapp_obj.route("/regis", methods=['GET','POST'])
def regis():
	if current_user.is_authenticated:
		return "<h1>you already logged in</h1>" 
	form = RegisForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None:
			u = User(username=form.username.data, email=form.email.data)
			u.set_password(password=form.password.data)
			db.session.add(u)
			db.session.commit()
			flash('user added')
			return redirect(url_for('login'))
		else:
			flash('user exist')
			return redirect(url_for('login'))

	return render_template('regis.html', title='Sign Up', form=form)


@myapp_obj.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))


@myapp_obj.route("/req")
# user needs to be logged in to see this page
# needs to be user route!
@login_required
# called view function
def req():
	return render_template('testReq.html')


@myapp_obj.route("/main_hidden_test")
@login_required
def main():
	return render_template('main.html')

#project page
@myapp_obj.route("/home", methods =["GET", "POST"])
@login_required
def home():
	form = ProjectForm()
	if form.validate_on_submit():
		project_id = str(uuid.uuid4())
		project = Project(id = project_id, project_name=form.project.data)
		db.session.add(project)
		db.session.commit()
		project_home(project_id)
		
	project_list = []

	for p in Project.query.all():
		new_p = {}
		new_p["id"] = p.id
		new_p["project_name"] = p.project_name
		project_list.append(new_p)

	return render_template('projects.html',project_list = project_list, form = form)







# project home page
@myapp_obj.route("/home/<project_id>", methods =["GET", "POST"])
@login_required
def project_home(project_id):
	form = TaskForm()
	print(current_user)
	if form.validate_on_submit():
		if form.task.data is None:
			print('empty')
		else:
			task = Tasks(task = form.task.data, priority = 1,project=project_id, user_id = current_user.id)
			db.session.add(task)
			db.session.commit()
	tasks = []
	for t in Tasks.query.filter_by(project=project_id).all():
		user = User.query.filter_by(id = t.user_id).first()
		new_t = {}
		new_t['user'] = user.username
		new_t['task'] = t.task
		tasks.append(new_t)
	return render_template('project_home.html',tasks = tasks, form = form)
