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

## USE CASE DESCRIPTIONS

Product Name: Task Managerinator

Problem Statement: The project allows users to manage a set of tasks and be able to collaborate and share tasks with other users.

Use Case Name: User able to change password

Date: 17 May, 2021

## Summary
The user can change the present password to another password in case they feel insecure or the password is hard to remember by confirming the present password.

## Actors
* Customers/Users
* System software

## Preconditions
* Precondition 1: The user must be logged in to their acount.
* Precondition 2: The user should click the 'User Settings' button in the navigation bar.
* Precondition 3: The user should click change password button.
* Precondition 4: The user should enter the valid current password in the text field.
* Precondition 4: The user should enter a valid new password and confirm the password in the text field.

## Triggers
* When the user clicks 'Change Password' button.

## Primary Sequence
* Step 1: Check if the user has successfully logged into their account.
* Step 2: Check if the current password entered is correct.
* Step 3: Check if the new password is valid.
* Step 4: Check if the confirm new password field matches the new password field.
* Step 5: Change the password for the associated account to the new password.
* Step 6: Store the new password associated with the account in the data base for future use and authentication.

## Primary Postconditions
* Postcondition 1: A new password for the associated account is created and stored in the data base.
* Postcondition 2: The user will be authenticated based on the new password.

## Alternate Sequence
NO  ALTERNATE SEQUENCE FOR THIS TASK SET.

-------------------------------------------------------------------------------------------------------------------------------------------------

## USE CASE DESCRIPTIONS

Product Name: Task Managerinator

Problem Statement: The project allows users to manage a set of tasks and be able to collaborate and share tasks with other users.

Use Case Name: Delete user account

Date: 17 May, 2021

## Summary
The user can delete their account permanently, with all their data, if they no longer require the services.

## Actors
* Customers/Users
* System software

## Preconditions
* Precondition 1: The user must be logged in to their acount.
* Precondition 2: The user should click the 'User Settings' button in the navigation bar.
* Precondition 3: The user should click 'Delete Account' button.
* Precondition 4: The user should enter the valid current password in the text field.
* Precondition 4: The user should enter a the current password to confirm in the text field.

## Triggers
* When the user clicks 'DELETE ACCOUNT FOREVER' button.

## Primary Sequence
* Step 1: Check if the user has successfully logged into their account.
* Step 2: Check if the current password entered is correct.
* Step 3: Check if the confirm password field matches the password field.
* Step 4: Delete the associated account forever by removing it from the data base.

## Primary Postconditions
* Postcondition 1: The associated account is deleted forever and the user is removed from the data base.

## Alternate Sequence
NO  ALTERNATE SEQUENCE FOR THIS TASK SET.

-------------------------------------------------------------------------------------------------------------------------------------------------

## USE CASE DESCRIPTIONS

Product Name: Task Managerinator

Problem Statement: The project allows users to manage a set of tasks and be able to collaborate and share tasks with other users.

Use Case Name: Set priority for task

Date: 17 May, 2021

## Summary
The user can prioritize the tasks between 1 and 3 so that the tasks with higher priority would be at the top helping the user know the important tasks.

## Actors
* Customers/Users
* System software

## Preconditions
* Precondition 1: The user must be logged in to their acount.
* Precondition 2: The user should be within a partcular project where the task is scheduled.
* Precondition 3: There should be at least one task to use the priority feature.
* Precondition 4: The user should click 'Prioritize Task' button.

## Triggers
* When the user clicks 'Prioritize Task' button.

## Primary Sequence
* Step 1: Check if the user has successfully logged into their account.
* Step 2: Check if the user has tasks within the project or can create a new one.
* Step 3: With every click on the 'Prioritize Task' button the priority of the task will alternate between 1 and 3.
* Step 4: Set the priority of the associated task to the desired value.

## Primary Postconditions
* Postcondition 1: The associated task will have a new priority and the data base is updated with the new priority.

## Alternate Sequence
NO  ALTERNATE SEQUENCE FOR THIS TASK SET.

-------------------------------------------------------------------------------------------------------------------------------------------------

## USE CASE DESCRIPTIONS

Product Name: Task Managerinator

Problem Statement: The project allows users to manage a set of tasks and be able to collaborate and share tasks with other users.

Use Case Name: Delete task

Date: 17 May, 2021

## Summary
The user can delete tasks that are no longer needed for the project to avoid having a long list with needless tasks.

## Actors
* Customers/Users
* System software

## Preconditions
* Precondition 1: The user must be logged in to their acount.
* Precondition 2: The user should be within a partcular project where the task is scheduled.
* Precondition 3: There should be at least one task scheduled to delete the task.
* Precondition 4: The user should click 'Delete Task' button.

## Triggers
* When the user clicks 'Delete Task' button.

## Primary Sequence
* Step 1: Check if the user has successfully logged into their account.
* Step 2: Check if the user has tasks within the project.
* Step 3: Delete the associated task by removing it from the data base.
* Step 4: Remove the associated task from the task list displayed.

## Primary Postconditions
* Postcondition 1: The associated task will be removed from the daa base and from the task lists.
* Postcondition 2: If there are more tasks in the list, the other task will take its place in the displayed list.

## Alternate Sequence
NO  ALTERNATE SEQUENCE FOR THIS TASK SET.

-------------------------------------------------------------------------------------------------------------------------------------------------

## USE CASE DESCRIPTIONS

Product Name: Task Managerinator

Problem Statement: The project allows users to manage a set of tasks and be able to collaborate and share tasks with other users.

Use Case Name: User reassign task

Date: 17 May, 2021

## Summary
The user can reassign a particular task to other users working on the project as long as the user exists in the data base. It can be used by managers and group leaders to assign tasks to different members in the group.

## Actors
* Customers/Users
* System software

## Preconditions
* Precondition 1: The user must be logged in to their acount.
* Precondition 2: The user should be within a partcular project where the task is scheduled.
* Precondition 3: There should be at least one task scheduled to reassign the task to another user.
* Precondition 4: The user being reassigned the task should exist in the data base and have a valid account.
* Precondition 5: The user must enter the name of the user to whom they want to assign the task in the text field associated with the task.
* Precondition 6: The user chould click 'Reassign Task' button.

## Triggers
* When the user clicks 'Reassign Task' button.

## Primary Sequence
* Step 1: Check if the user has successfully logged into their account.
* Step 2: Check if the user has tasks within the project.
* Step 3: Check if the user entered to be reassigned is a valid user and exists in the data base.
* Step 4: Reassign the associated task to the other user with set deadline and priority.
* Step 5: Add the changes to the data base and display the task with a new user in the task list.

## Primary Postconditions
* Postcondition 1: The associated task will be assigned to a different user and added to the data base to display in the task list.

## Alternate Sequence
NO  ALTERNATE SEQUENCE FOR THIS TASK SET.

-------------------------------------------------------------------------------------------------------------------------------------------------

## USE CASE DESCRIPTIONS

Product Name: Task Managerinator

Problem Statement: The project allows users to manage a set of tasks and be able to collaborate and share tasks with other users.

Use Case Name: Create multiple projects

Date: 17 May, 2021

## Summary
The user can create multiple projects based on their requirements to work on. They can have projects associated with their work and their personal projects. The userscan keep tasks separated for each project and ewitch between the projects to track their progress over time.

## Actors
* Customers/Users
* System software

## Preconditions
* Precondition 1: The user must be logged in to their acount.
* Precondition 2: The user should be at the home page of the application.
* Precondition 3: There should be at least one project scheduled to create multiple projects by the user.
* Precondition 4: The user should enter the name of the project in the text field provided.
* Precondition 5: The user chould click 'Add Project' button.

## Triggers
* When the user clicks 'Add Project' button while at least one project exists in the data base.

## Primary Sequence
* Step 1: Check if the user has successfully logged into their account.
* Step 2: Check if the user has at least one project predefined.
* Step 3: Check if the user entered a valid project name.
* Step 4: Add the new project to the data base and display on the list of projects.

## Primary Postconditions
* Postcondition 1: The new project will be created along with the old projects exising in the data base.
* Postcondition 2: The new project is displayed on the home page and allows same functionalities as all other projects.

## Alternate Sequence
NO  ALTERNATE SEQUENCE FOR THIS TASK SET.

-------------------------------------------------------------------------------------------------------------------------------------------------









12.View all tasks page
	*

13.Delete all completed tasks
	*

14.Add readme to projects
	*

15.Real-Time notifications
	*
