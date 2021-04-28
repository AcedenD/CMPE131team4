# same as
# from app import db
from app import db
from datetime import datetime
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=False)
    email = db.Column(db.String(32), unique=True, nullable=False, index=True)
    password = db.Column(db.String(200), unique=False)

    tasks = db.relationship('Tasks', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


    def __repr__(self):
        return '<User {}>'.format(self.username)

class Project(db.Model):
    id = db.Column(db.String(256), primary_key=True)
    project_name = db.Column(db.String(256))
   

    

    def __repr__(self):
        return self.project_name
    

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(256))
    # priority is level 1-3; 1 is least important , and 3 is most important
    priority = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # To find what project each task belongs too 
    project = db.Column(db.String(256))
    

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        user = User.query.filter_by(id = self.user_id).first()
        return f'<Task: {self.task} created by {user}>'

    def set_priority(self, priority):
        self.priority = priority





@login.user_loader
def load_user(id):
    return User.query.get(int(id))
