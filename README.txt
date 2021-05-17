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
	On the tasks page, user can create new project, set priority, mark as 
  completed, delete the task and reassign the task to another user(if 
  the user exists). 
The navigation bar on the top of every page:
	Logo on the right, which will take the user back to the home page.
	Logout button, when user decide to logout.
	Calendar button, where user can see all the task and it due date.
	UserSetting button, which takes the user to the user setting page. 
  The page has 3 buttons:
		Change Password button, that redirects the user to a page where 
    they can change their account password.
		Delete account button, that redirects the user to a page where 
    they can delete their account forever.
		Time log button, that redirects the user to a time log page to 
    show the user's login and logout time.

For step-by-step guide look into "Navigating through project and how to use the app" below in the README file.

