from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required

from app import myapp_obj
from app import db
from app.forms import LoginForm, RegisForm

from app.models import User

# different URL the app will implement
@myapp_obj.route("/")
# called view function
@login_required
def hello():
    user = {'name' : 'Miguel (made with Dictionary)'}
    posts = [
        {
            'author' : 'Linh',
            'body' : 'Beautiful day in San Jose!'
        },
        {
            'author': 'Emma',
            'body' : 'I got my vaccine today!'
        }
    ]

    return render_template('hello.html', user_template=user, posts=posts)

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
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
#        next_page = request.args.get('next')
#        if not next_page or url_parse(next_page).netloc != '':
        next_page = url_for('req')

        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)


@myapp_obj.route("/regis", methods=['GET','POST'])
def regis():
    form = RegisForm()
    if form.validate_on_submit():
      user = User.query.filter_by(username=form.username.data).first()
      if user is None:
         u = User(username=form.username.data, email=form.email.data)
         u.set_password(password=form.password.data)
         db.session.add(u)
         db.session.commit()
         flash('user added')
      else:
         flash('user exist')

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