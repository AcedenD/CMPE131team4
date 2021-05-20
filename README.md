# CMPE131team4

## Task Managerinator

## Description

The task manager application helps the users track multiple projects with set priorities and allows users to assign tasks to other users.
Users can create new projects with assigned tasks, delete tasks or delete when tasks are marked as completed and set priority for each tasks. 
The application can list all the tasks so the user can click on the desired task to visit project link. The application features a central 
calendar to keep a visual track of the project tasks and due dates once the tasks are created. It also features an online time tracker, 
which logs in the user when they log in to their portal and log out when they log out of the portal. The feature can be used by supervisors 
to track the payroll and help users track their working time on projects. The application allows the user to add a read me file for their 
projects for a description and sends a real-time notification to users about the tasks and due dates. The task manager portal allows 
features such as creating account for the user, allowing user to change password, and delete user account.

## Table of contents

* [How to download the app](#how-to-download-the-app)
* [How to run app](#how-to-run-app)
* [General instructions for website](#general-instructions-for-website)
* [Dependencies](#dependencies)
* [External Tools](#external-tools)
* [Use Case](#use-cases)
* [Navigating through project and how to use the app](#navigating-through-project-and-how-to-use-the-app)
* [Credits](#credits)
* [License](#License)
* [How to contribute to the project](#how-to-contribute-to-the-project)
* [Tests for the project](#tests-for-the-project)
* [Conclusion](#conclusion)
* [Contact us](#contact-us)

## How to download the app

Download or pull the files from AcedenD/CMPE131team4 through github at 
a local repository on your machine.

Github link to clone project: https://github.com/AcedenD/CMPE131team4.git 

## How to run app

* python3 run.py
* ### If problems occur try recreating the database 
* python3 
* >>>from app import db
* >>>db.create_all()

The commands above depends on the version of python running on local machine. If using python 3 then use the above command else change accordingly.
Once the server link is generated in the terminal, copy the local host to the desired browser and the app will start.

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

To install pip (Unix/Mac or Windows) and documentation on pip refer to the 
link: https://pip.pypa.io/en/stable/installing/

## External Tools

The tools were used to view the database items: 
* SQLite Database viewer https://sqliteonline.com/
* https://inloop.github.io/sqlite-viewer/

## Use Cases
 
- 1.Create account
	* When user first come on the app, they will not be able to sign in since they don't have an account.
	* User then can press on the Sign Up button, fill in the information and press Sign Up to create an account.
- 2.Create project
- 3.Create task
	* After clicking on a project from the home page, user will be met with a rask form and a black table.
	* User then can type in the task, due date and press add task to add the task. The page will reload and the table now should have that task.
- 4.Central Calender
- 5.Track online time
	* The user should go to user setting in the navigation bar on top-right corner of every page.
	* The user should click the time log button - third on the list.
	* The user will be able to see their login time - the time stamp when they logged in, and log out time - the time when they logged out of the account, along with the total time worked which is calculated as a difference between the log in time and the log out time to show the user how long they worked online.
	* The user must login and logout at least once before they can see their times stamps on the list. First time users will see a blank list.
- 6.User able to change password
	* In the UserSetting, user have the option to change their password.
	* When clicked on the change password, user will be met with a form with 3 inputs on it.
	* User then must enter in their current password, new password and new password confirmation.
	* If the old password match with the current password and new password match with new password confirmation, and when they press change password.
	* The page will reload and their password sucessfully change.
- 7.Delete User Account
	* In the UserSetting, user have the option to delete account
	* When clicked on the delete account, user will be redirected to a page with a from with 2 inputs on it.
	* The user will enter their current password in the first input and enter it again for the second input.
	* If the two input match with the current password when user press the delete account forever button, they will be redirect to the login page with a message that the account deleted successfully. 
- 8.Set priority for task
	* When user want to change the priority of a task, on the tasks page, user can click on prioritized task
	* If the current priority is 1 then it will change to 3, be red and bold.
	* If the current priority is 3 then it will change to 1 and return to black and unbold.
- 9.Delete Task
	* When user want to delete a task,on the tasks page, they can press the delete task button, the page will reload with the updated table of tasks.
- 10.User reassign task
	* If user want to reasssign a task to another user, they can choose the task that they  want to reassign on the tasks page
	* Type in the user that they want to reassign to and press reassign task.
	* If the entered user exist, the task will be reassign to them and the table will update
	* If the entered user doesn't exist, the page will give an message that user doesn't exit
- 11.Create multiple projects
- 12.View all tasks page
	* On the home page, in addition to showing all the projects, there is a button where user can click on and be redirected to a page with all the current tasks.
- 13.Delete all completed tasks
	* On the view all tasks page, user have the option to delete all completed tasks.
	* When user click on the delete all completed tasks, for all of the tasks that are marked completed = True, those will be deleted. 
	* The view all tasks will reload and now should only show incompleted tasks
- 14.Add readme to projects
- 15.Real-Time notifications

## Navigating through project and how to use the app

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

## Credits

Thanks to the members for making the project a success:

	1) Aden Dang - https://github.com/AcedenD
	2) Aishwar Gupta - https://github.com/Aishwar-Gupta
	3) Jugad Khajuria - https://github.com/JugadK
	4) Khanh Nguyen - https://github.com/khanhng21


## License

Proprietary license.
*The work cannot be modified or redistributed without permission.

## How to contribute to the project

In order to contribute to the project or to report bugs use github through the link below and open a pull request with a description message 
and one of the members would look into the issue.

github link: https://github.com/AcedenD/CMPE131team4.git

* Steps involved:
	* Fork the repository on your local machine
	* Add the necessary changes to contribute to the project or bugs report
	* Stage the files to the local repository - git add .
	* Commit the changes to the local repository with appropriate message - git commit -m '<message>'
	* Open a pull request - git pull

*Members would look into the issue within a week.

## Tests for the project

The files in the project includes two files named "user_test.py" and "task_test.py" which test the user and the task functions respectively. 
It does so by passing a demo user and task object and check to match in the database. 
Each function is tested twice and users can run the test with the commands below to test the app.

	python3 user_test.py
	python3 task_test.py

The commands above depends on the version of python running on local machine.
If using python 3 then use the above command else change accordingly.
On the local repository, the user can pass their own values for the user object and run the tests.

## CONCLUSION

The application is used to track online projects, personal or work, and manage resources to stay on top of the requirements.
The project offers easy visualizations of projects through text and calendars to track deadlines and total time worked online. 
The app has a fast response time and redirects the user to various pages depending on the clicks and authentication. 
Multiple users can collaborate over multiple projects by assigning tasks accordingly through the app. 
The unique features and easy user interface makes the app stand out in the community and help users and supervisors manage their projects.


## CONTACT US

Please use DISCORD or EMAIL to contact us:
* Aden Dang - adendd - adendd@taskmanagerinator.com
* Aishwar Gupta - Aishwar - aishwar@taskmanagerinator.com
* Jugad Khajuria - Jewgad - jewgad@taskmanagerinator.com
* Khanh Nguyen - Khanh Nguyen - khanh_nguyen@taskmanagerinator.com

- You can also email your concerns at concerns@taskmanagerinator.com


-------------------------Thank-you-for-using-our-software-------------------------
