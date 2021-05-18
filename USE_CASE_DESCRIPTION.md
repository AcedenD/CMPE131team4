## USE CASE DESCRIPTIONS

Product Name: Task Managerinator

Problem Statement: The project allows users to manage a set of tasks and be able to collaborate and share tasks with other users.

Use Case Name: Create account

Date: 17 May, 2021

## Summary
The users should be able to create an account on the portal so they can use other features and save their future works and progress in one dashboard. 
The account will keep track of all the schedules and will allow the user to schedule tasks.

## Actors
* Customers/Users
* System software

## Preconditions
* Precondition 1: The user must choose "Sign up" button.
* Precondition 2: The user should enter a valid Username.
* Precondition 3: The user should enter a valid Email Address.
* Precondition 4: The user should enter a valid Password.
* Precondition 5: The user should not exist in the database.

## Triggers
* The user must choose Sign up button in order to sign up for a new account.

## Primary Sequence
* Step 1: Check the entered Username, email, and password are valid and the user does not exit in the data base.
* Step 2: Create a new user and store it in the data base with the specified attributes.

## Primary Postconditions
* Postcondition 1: A new user is created and stored in the data base.

## Alternate Sequence
NO  ALTERNATE SEQUENCE FOR THIS TASK SET.

-------------------------------------------------------------------------------------------------------------------------------------------------

## USE CASE DESCRIPTIONS

Product Name: Task Managerinator

Problem Statement: The project allows users to manage a set of tasks and be able to collaborate and share tasks with other users.

Use Case Name: Create project

Date: 17 May, 2021

## Summary
The users should be able to create projects to make a collection of tasks required for a particular project so the tasks do not mix.  
The projects will help keep track of all the schedules for a particular set of tasks and will allow the user to schedule tasks.

## Actors
* Customers/Users
* System software

## Preconditions
* Precondition 1: The user must be logged in to their portal.
* Precondition 2: The user must write a project name in the text field.
* Precondition 3: The user should click "Add project" button.
* Precondition 4: The project name should not match with an existing project in the data base.

## Triggers
* The user must enter a project name in the text field.
* The user must click the "Add project" button for creating a new project.

## Primary Sequence
* Step 1: Check if the user is logged in to their account. 
* Step 2: Check if the user entered a valid project name in the text field that does not exit in the data base.
* Step 3: Create a new project and store it in the data base with the specified attributes.

## Primary Postconditions
* Postcondition 1: A new project is created and stored in the data base.
* Postcondition 2: Display the new project on the home page.

## Alternate Sequence
* NO  ALTERNATE SEQUENCE FOR THIS TASK SET.

-------------------------------------------------------------------------------------------------------------------------------------------------

## USE CASE DESCRIPTIONS

Product Name: Task Managerinator

Problem Statement: The project allows users to manage a set of tasks and be able to collaborate and share tasks with other users.

Use Case Name: Create task

Date: 17 May, 2021

## Summary
The users can create tasks according to their schedule, on a particular date and time, and set the priority of the task to keep track of the work to be done.
The user can create multiple tasks within a project and will be able to assign tasks to other users provided the user exists. The user can track deadlines, save
work for future, and manage progress from one dashboard. 

## Actors
* Customers/Users
* System software
* System clock
* System calendar

## Preconditions
* Precondition 1: The user must be logged in to their acount.
* Precondition 2: The user must be within a valid project.
* Precondition 3: The user should enter a valid task name in the text field.
* Precondition 4: The user should enter a valid due date in the format MM/DD/YYYY.

## Triggers
* The user must click Add Task button in order to generate a new task.

## Primary Sequence
* Step 1: Check if the user is inside a project.
* Step 2: Validate the entered task name and due date in the correct format.
* Step 3: Create a new task with specified name and due date, and store the task in the data base.
* Step 4: Add the task to the calendar with due date.
* Step 5: Display the task at the bottom in the task list with set priority and due date.

## Primary Postconditions
* Postcondition 1: A new task is created and stored in the data base.
* Postcondition 2: The task due date is added to the central calendar.
* Postcondition 3: The task is displayed in the task list with set priority, name, and due date.

## Alternate Sequence
NO  ALTERNATE SEQUENCE FOR THIS TASK SET.

-------------------------------------------------------------------------------------------------------------------------------------------------

## USE CASE DESCRIPTIONS

Product Name: Task Managerinator

Problem Statement: The project allows users to manage a set of tasks and be able to collaborate and share tasks with other users.

Use Case Name: Central calendar

Date: 18 May, 2021

## Summary
The users can have a calendar view of the deadlines to plan their time spent on tasks. The calendar will allow the users to add new tasks.
The user selects a particular date and enters the start and end time of the task to schedule the task on that day.

## Actors
* Customers/Users
* System software
* System clock
* System calendar

## Preconditions
* Precondition 1: The user must be logged in to their account.
* Precondition 2: The user must choose the "Calendar" button on the top at the navigation bar.

## Triggers
* The user must click the "Calendar" button in order to be redirected to the calendar page for the new account.

## Primary Sequence
* Step 1: Check if the calendar button was clicked in the navigation bar.
* Step 2: Upload the calendar and add the tasks from the data base on specified dates.
* Step 3: If user want to add a new task, then add the task to the data base on the specified date.

## Primary Postconditions
* Postcondition 1: A calendar view is available to the user with marked tasks and deadlines.
* Postcondition 2: If new task is added, then the task is added to the data base with specified attributes and will display in task list.

## Alternate Sequence
NO  ALTERNATE SEQUENCE FOR THIS TASK SET.

-------------------------------------------------------------------------------------------------------------------------------------------------

## USE CASE DESCRIPTIONS

Product Name: Task Managerinator

Problem Statement: The project allows users to manage a set of tasks and be able to collaborate and share tasks with other users.

Use Case Name: Track online time

Date: 17 May, 2021

## Summary
The feature allows the users to track time spent online. It logs in the user once they log into their account and logs out when they log out of their account.
The feature can be used by users to track their time spent on various personal projects or allow the supervisor complete the payroll through hours worked.

## Actors
* Customers/Users
* System software
* System clock
* System calendar

## Preconditions
* Precondition 1: The user must be logged in to their acount.
* Precondition 2: The user must be logged in and logged out at least once or else the data base would be empty.
* Precondition 3: The user should click the 'User Settings' button in the navigation bar.
* Precondition 4: The user should click 'Time Log' button to view the past entries.

## Triggers
* When the user logs in and logs out of their account.

## Primary Sequence
* Step 1: Check if the user has successfully logged into their account.
* Step 2: Store the time stamp when the user logged into their account.
* Step 3: Check if the user has logged out of the account.
* Step 4: Store the time stamp when the user logged out of their account.
* Step 5: Calculate the total time worked by taking the time difference and store it in the data base.
* Step 6: When 'Time Log' button is clicked, display the past entries of the user.

## Primary Postconditions
* Postcondition 1: A new time stamp for log in and log out is created and stored in the data base.
* Postcondition 2: The calculated online time is added to the data base.
* Postcondition 3: The time log data base is displayed with respective date and time.

## Alternate Sequence
NO  ALTERNATE SEQUENCE FOR THIS TASK SET.

-------------------------------------------------------------------------------------------------------------------------------------------------



6.User able to change password
	*

7.Delete User Account
	*

8.Set priority for task
	*

9.Delete Task
	*

10.User reassign task
	*

11.Create multiple projects
	*

12.View all tasks page
	*

13.Delete all completed tasks
	*

14.Add readme to projects
	*

15.Real-Time notifications
	*
