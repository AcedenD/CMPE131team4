from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
import uuid

from datetime import datetime

from app import myapp_obj
from app import db

from app.forms import LoginForm, RegisForm, ProjectForm, TaskForm, ChangePasswordForm, DeleteAccountForm, ReassignedTask


from app.models import User, Tasks, Project, Schedule


@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect("/home") 
	form = LoginForm()
	if form.validate_on_submit():
		current_user.last_login = datetime.utcnow()
		db.session.commit()
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
			u.last_login = datetime.utcnow()
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
	current_user.last_logout = datetime.utcnow()
	print(current_user.last_logout)
	print(current_user.last_login)
	print(current_user.last_logout- current_user.last_login)
	schedule = Schedule(user_id=current_user.id, total_time=(current_user.last_logout - current_user.last_login),login=current_user.last_login,logout=current_user.last_logout)
	db.session.add(schedule)
	db.session.commit()

	logout_user()
	return redirect(url_for('login'))


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

@myapp_obj.route("/time", methods =["GET", "POST"])
@login_required
def timetracker():
	form = ProjectForm()
	print(current_user.last_login)
	schedule_list = Schedule.query.filter_by(user_id = current_user.id)
#	for p in Schedule.query.all():
#		schedule_list.append(p)
#	print(schedule_list)


	return render_template('time.html',schedule_list = schedule_list)



# project home page
@myapp_obj.route("/home/<project_id>", methods =["GET", "POST"])
@login_required
def project_home(project_id):
	reassign = ReassignedTask()
	form = TaskForm()
	print(current_user)
	if form.validate_on_submit():

		if form.task.data is None:
			print('empty')
		else:
			print('test2')
			date_time_obj = datetime.strptime(form.due_date.data, '%m/%d/%Y')
			task = Tasks(task = form.task.data, priority = 1,project=project_id, user_id = current_user.id, due_date = date_time_obj, user = current_user.username, completed = False)
			db.session.add(task)
			db.session.commit()
#	tasks = []
	tasks = Tasks.query.filter_by(project = project_id)
	print('project: ', project_id )
	current_project =  Project.query.filter_by(id = project_id).first().project_name

	return render_template('project_home.html',tasks = tasks, form = form, reassign = reassign, current_project = current_project)


# detele task
@myapp_obj.route("/deleteTask/<task_id>/<project_id>", methods =["GET", "POST"])
@login_required
def delete_task(task_id, project_id):
	print(project_id)
	task = Tasks.query.filter_by(id = task_id, project = project_id).first()
	if task is not None:
		db.session.delete(task)
		db.session.commit()

	return redirect(url_for('project_home', project_id = project_id))


#prioritize task
@myapp_obj.route("/prioritizeTask/<task_id>/<project_id>", methods =["GET", "POST"])
@login_required
def change_priority(task_id, project_id):
    print(project_id)
    task = Tasks.query.filter_by(id = task_id, project = project_id).first()
    if task is not None:
        task.priority = 3
        db.session.add(task)
        db.session.commit()

    return redirect(url_for('project_home', project_id = project_id))


#complete task
@myapp_obj.route("/completeTask/<task_id>/<project_id>", methods =["GET", "POST"])
@login_required
def complete_task(task_id, project_id):
    print(project_id)
    task = Tasks.query.filter_by(id = task_id, project = project_id).first()
    if task is not None:
        task.completed = True
        db.session.add(task)
        db.session.commit()

    return redirect(url_for('project_home', project_id = project_id))


#reassign task
@myapp_obj.route("/reassignedTask/<task_id>/<project_id>", methods =["GET", "POST"])
@login_required
def reassign_task(task_id, project_id):
	reassign = ReassignedTask()
	if reassign.validate_on_submit():
		user = User.query.filter_by(username = reassign.user.data).first()
		if user is not None:
			task = Tasks.query.filter_by(id = task_id, project = project_id).first()
			print(user,task)
			task.user_id = user.id
			task.user = user.username
			db.session.add(task)
			db.session.commit()
		else:
			flash('enter an existing user')

	return redirect(url_for('project_home', project_id = project_id))






# calendar page
@myapp_obj.route("/calendar", methods =["GET", "POST"])
@login_required
def calendar():
	return render_template('calendar.html')




# user setting
@myapp_obj.route("/userSetting")
@login_required
def user_setting():
	return render_template('userSetting.html')


# change password
@myapp_obj.route('/changePassword',methods=['GET','POST'])
@login_required
def change_password():
	user = User.query.filter_by(id = current_user.id).first()
	form = ChangePasswordForm()
	print(user)
	if form.validate_on_submit():
		if user.check_password(form.old_password.data) and (form.old_password.data != form.new_password.data)  and (form.new_password.data == form.new_password_confirm.data):
			user.set_password(form.new_password.data)
			db.session.commit()
			return redirect(url_for('user_setting'))

	return render_template('changePassword.html', form = form)



# delete account
@myapp_obj.route('/deleteAccount', methods=['GET','POST'])
@login_required
def delete_account():
	user = User.query.filter_by(id = current_user.id).first()
	form = DeleteAccountForm()
	if form.validate_on_submit():
		if user.check_password(form.password.data) and (form.password.data == form.password_confirm.data):
			logout_user()
			db.session.delete(user)
			db.session.commit()
			flash('Account Deleted Successfully!')
			return redirect(url_for('login'))
		else:
			flash('Wrong password')
	return render_template('deleteAccount.html', form = form)
