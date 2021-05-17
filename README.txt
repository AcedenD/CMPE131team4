PROJECT NAME: Task Managerinator


DESCRIPTION:
The task manager application helps the users track multiple projects
with set priorities and allows users to assign tasks to other users.
Users can create new projects with assigned tasks, delete tasks or 
delete when tasks are marked as completed and set priority for each 
tasks. The application can list all the tasks so the user can click
on the desired task to visit project link. The application features
a central calendar to keep a visual track of the project tasks and 
due dates once the tasks are created. It also features an online time
tracker, which logs in the user when they log in to their portal and 
log out when they log out of the portal. The feature can be used by 
supervisors to track the payroll and help users track their working 
time on projects. The application allows the user to add a read me 
file for their projects for a description and sends a real-time 
notification to users about the tasks and due dates. The task manager
portal allows features such as creating account for the user, allowing
user to change password, and delete user account.


TABLE OF CONTENT:
1) How to download the app.
2) How to run app.
3) General instructions for using the website.
4) Dependencies.
5) External tools.
6) Use cases.
7) Navigating through project and how to use the app.
8) Credits.
9) License.
10) How to contribute to the project.
11) Tests for the project.
12) Conclusion.
13) Contact us.


HOW TO DOWNLOAD THE APP:
Download or pull the files from AcedenD/CMPE131team4 through github at 
a local repository on your machine.

Github link to clone project: https://github.com/AcedenD/CMPE131team4.git 


HOW TO RUN THE APP:
Once the files are downloaded, go to the local repository and run the 
following command in the terminal:

python3 run.py

In case of problems, try recreating the database through the following 
commands:

python3
>>> from app import db
>>> db.create_all()

The commands above depends on the version of python running on local 
machine. If using python 3 then use the above command else change 
accordingly.
Once the server link is generated in the terminal, copy the local host 
to the desired browser and the app will start.


GENERAL INSTRUCTIONS FOR USING THE WEBSITE:
When the users are at the login page, but do not have an account in 
Task Managerinator, they can create a new account through the sign up 
button.
Once the user logs in successfully, the home page is shown with all 
the current projects.
  If there are no projects or if the user wants to create a new project 
  then enter the project name followed by the create project button on 
the home page.
With at least one project on dashboard, the user can click on the 
project to go to the tasks page.
	On the tasks page, user can create new project, set priority, 
	mark as completed, delete the task and reassign the task to 
	another user(if the user exists). 
The navigation bar on the top of every page:
	Logo on the right, which will take the user back to the home page.
	Logout button, when user decide to logout.
	Calendar button, where user can see all the task and it due date.
	UserSetting button, which takes the user to the user setting page. 
  The page has 3 buttons:
		Change Password button, that redirects the user to a page 
		where they can change their account password.
		Delete account button, that redirects the user to a page 
		where they can delete their account forever.
		Time log button, that redirects the user to a time log page
		to show the user's login and logout time.

For step-by-step guide look into "Navigating through project and how to use
the app" below in the README file.


DEPENDENCIES:

pip/pip3 install flask flask-wtf flask-sqlalchemy flask-login

To install pip (Unix/Mac or Windows) and documentation on pip refer to the 
link: https://pip.pypa.io/en/stable/installing/


EXTERNAL TOOLS:
External tools were used to view the database items:
	SQLite Database viewer https://sqliteonline.com/
	Alternative viewer: https://inloop.github.io/sqlite-viewer/


USE CASES:

	1. Create account
	2. Create project
	3. Create task
	4. Central Calendar
	5. Track online time
	6. User able to change password
	7. Delete User Account
	8. Set priority for task
	9. Delete Task
	10. User reassign task
	11. Create multiple projects
	12. View all tasks page - able to click on task to visit project
	13. Delete all completed tasks
	14. Add readme to projects
	15. Real-Time notifications


NAVIGATING THROUGH PROJECT AND HOW TO USE THE APP:
First time users should follow these steps to better understand the 
app and get familiar:
1) When running for the first time the user must create an account 
through "Sign up" button.
	Enter your Username
	Enter your Email address
	Enter your Password
And click "Sign up" Now the account is created with Task Managerinator 
which users can use for future.

2) Log in to your account using your credentials:
	Enter Username
	Enter Password
and click "login" which will redirect the user to the home page.

3) The home page lists the projects that were created and is blank if 
there are no projects. The user can add new projects by entering the 
name of the project in the text field and click the "Add Project" 
button. The user can check all the tasks scheduled through the 
"View All Tasks" button.

4) Every page after the user is logged in has a navigation bar on the top 
which features a logo on the left which the user can use to return to the 
home page from any other page of the application. On the right side are 
three buttons:
	Logout - helps the user log out of the portal at Task Managerinator.
	Calendar - which open up the calendar view for the user to add task,
	track tasks, and track deadlines.
	User Setting - which redirects the user to the settings page.

5) The user can click on a particular project to be redirected to a page 
with the list of tasks and due dates associated with the project. It lists 
the  user and the priority of the task along with a field to reassign the 
task if the user exists through the "Reassign Task" button. The user can 
prioritize the task through "Prioritize Task" button. The user can also 
mark the task as completed through "Complete Task" button or delete the 
task with "Delete Task" button.

6) The user can add new tasks with in a particular project by entering the
name of the task in the text field followed by the due date for the task in
the format - MM/DD/YYYY and click "Add Task" which can be viewed at the 
bottom list. 
Please match the format of the date as it is required to match in order to
create a new task.

7) The calendar page offers the user a visual representation of the tasks 
and deadlines hrough a calendar view. The user can add new tasks by clicking
on the date and the "+" button which will prompt the user to enter a start 
and end time for the task to be scheduled.

8) The user settings page has three buttons:
	Change password - Enter current password followed by new password 
	and click "Change Password" button.
	Delete account - Enter current password, confirm, and then click 
	"DELETE ACCOUNT FOREVER" button.
	Time Log - Shows the login and log out time of the user along with
	the total time worked online.
*First time users would see a blank space as they have logged in for the 
first time and the database is empty. 


CREDITS:
Thanks to the members for making the project a success:

1) Aden Dang - https://github.com/AcedenD
2) Aishwar Gupta - https://github.com/Aishwar-Gupta
3) Jugad Khajuria - https://github.com/JugadK
4) Khanh Nguyen - https://github.com/khanhng21


LICENSE:
Proprietary license.
The work cannot be modified or redistributed.


HOW TO CONTRIBUTE TO THE PROJECT:
In order to contribute to the project or to report bugs use github through 
the link below and open a pull request with a description message and one 
of the members would look into the issue.

github link: https://github.com/AcedenD/CMPE131team4.git

Steps involved:
	Fork the repository on your local machine
	Add the necessary changes to contribute to the project or bugs report
	Stage the files to the local repository - git add .
	Commit the changes to the local repository with appropriate 
	message - git commit -m '<message>'
	Open a pull request - git pull

Members would look into the issue within a week.


TESTS FOR THE PROJECT:
The files in the project includes two files named "user_test.py" and 
"task_test.py" which test the user and the task functions respectively. It 
does so by passing a demo user and task object and check to match in the 
database. Each function is tested twice and users can run the test with 
the commands below to test the app.

python3 user_test.py
python3 task_test.py

The commands above depends on the version of python running on local machine.
If using python 3 then use the above command else change accordingly.
On the local repository, the user can pass their own values for the user 
object and run the tests.

