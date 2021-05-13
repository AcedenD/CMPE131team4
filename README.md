# CMPE131team4

## Table of contents
* [How to run app](#how-to-run-app)
* [General instructions for website](#general-instructions-for-website)
* [Dependencies](#dependencies)
* [External Tools](#external-tools)
* [Use Case](#use-cases)

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
