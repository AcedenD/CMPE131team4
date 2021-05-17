# CMPE131team4

## Table of contents
* [How to run app](#how-to-run-app)
* [General instructions for website](#general-instructions-for-website)
* [Dependencies](#dependencies)
* [External Tools](#external-tools)
* [Use Case](#use-cases)

## HOW TO DOWNLOAD THE APP:
Download or pull the files from AcedenD/CMPE131team4 through github at 
a local repository on your machine.

Github link to clone project: https://github.com/AcedenD/CMPE131team4.git 

## How to run app

* python3 run.py
* ### If problems occur try recreating the database 
* python3 
* >>>from app import db
* >>>db.create_all()

## General instructions for website

* When user are in the login page, if they don't have an account they can press on sign up to create one.
* If user were successfully login, they will reach the home page where all the current projects are shown.
  * If no project shown, user can create a new project by enter in a name and press create project.
* Once at least one project is shown, user can click on it and it will take the user to the tasks page for the project.
  * On the tasks page user can create new project, prioritize, mark complete, delete the task and reassign the task to another user(if user exist).
* On top of most of the page is a navigation bar.
  * On the navigation bar there is a logo on the right where user can press and it will take the user back to the home page.
  * A Logout button, when user decide to logout.
  * A Calendar button where user can see all the task and it due date.
  * A UserSetting button will take the user to the user setting page.
    * In the user setting page there are three addition buttons user can press.
      * A change password button that will redirect the user to a page where they can change their password.
      * A Delete account button that will redirect them to a page where they can delete their account forever.
      * A Time log button that take the user to a time log page where it show the user's login and logout time.

## Dependencies

* pip/pip3 install flask flask-wtf flask-sqlalchemy flask-login

## External Tools

* SQLite Database viewer https://sqliteonline.com/
* https://inloop.github.io/sqlite-viewer/

## Use Cases
 
- 1.Create account
- 2.Create project
- 3.Create task
- 4.Central Calender
- 5.Track online time
- 6.User able to change password
- 7.Delete User Account
- 8.Set priority for task
- 9.Delete Task
- 10.User reassign task
- 11.Create multiple projects
- 12.View all tasks page
- 13.Delete all completed tasks
- 14.Add readme to projects
- 15.Real-Time notifications

## NAVIGATING THROUGH PROJECT AND HOW TO USE THE APP:
First time users should follow these steps to better understand the app and get familiar:
1) When running for the first time the user must create an account through "Sign up" button.
	 * Enter your Username
	 * Enter your Email address
	 * Enter your Password
And click "Sign up" Now the account is created with Task Managerinator which users can use for future.

2) Log in to your account using your credentials:
	 * Enter Username
	 * Enter Password
and click "login" which will redirect the user to the home page.

3) The home page lists the projects that were created and is blank if there are no projects. 
The user can add new projects by entering the name of the project in the text field and click the "Add Project" button. 
The user can check all the tasks scheduled through the "View All Tasks" button.

4) Every page after the user is logged in has a navigation bar on the top which features a logo 
on the left which the user can use to return to the home page from any other page of the application.
On the right side are three buttons:
	 * Logout - helps the user log out of the portal at Task Managerinator.
	 * Calendar - which open up the calendar view for the user to add task, track tasks, and track deadlines.
	 * User Setting - which redirects the user to the settings page.

5) The user can click on a particular project to be redirected to a page with the list of tasks and due dates 
associated with the project. It lists the  user and the priority of the task along with a field to reassign the 
task if the user exists through the "Reassign Task" button. The user can prioritize the task through "Prioritize Task" button.
The user can also mark the task as completed through "Complete Task" button or delete the task with "Delete Task" button.

6) The user can add new tasks with in a particular project by entering the name of the task in the text field followed by the due date for
the task in the format - MM/DD/YYYY and click "Add Task" which can be viewed at the bottom list. 
 * Please match the format of the date as it is required to match in order to create a new task.

7) The calendar page offers the user a visual representation of the tasks and deadlines hrough a calendar view. 
The user can add new tasks by clicking on the date and the "+" button which will prompt the user to enter a start 
and end time for the task to be scheduled.

8) The user settings page has three buttons:
	 * Change password - Enter current password followed by new password and click "Change Password" button.
	 * Delete account - Enter current password, confirm, and then click "DELETE ACCOUNT FOREVER" button.
	 * Time Log - Shows the login and log out time of the user along with the total time worked online.
*First time users would see a blank space as they have logged in for the first time and the database is empty. 

## CREDITS:
Thanks to the members for making the project a success:

	1) Aden Dang - https://github.com/AcedenD
	2) Aishwar Gupta - https://github.com/Aishwar-Gupta
	3) Jugad Khajuria - https://github.com/JugadK
	4) Khanh Nguyen - https://github.com/khanhng21


## LICENSE:
Proprietary license.
*The work cannot be modified or redistributed without permission.


## HOW TO CONTRIBUTE TO THE PROJECT:
In order to contribute to the project or to report bugs use github through the link below and open a pull request with a description message 
and one of the members would look into the issue.

github link: https://github.com/AcedenD/CMPE131team4.git

*Steps involved:
	* Fork the repository on your local machine
	* Add the necessary changes to contribute to the project or bugs report
	* Stage the files to the local repository - git add .
	* Commit the changes to the local repository with appropriate message - git commit -m '<message>'
	* Open a pull request - git pull

*Members would look into the issue within a week.

