Git link: https://github.com/AcedenD/CMPE131team4.git
-Aden Dang (AcedenD)
-Aishwar Gupta (Aishwar-Gupta)
-
-

Project Name: TasK Managerinator (might change)

USE CASES:

1) Create account
2) Schedule Meetings and Events
3) Create Task
4) Set Task Priority 
5) Central Calendar
6) Text Channels
7) Progress Reports 
8) Real Time Notification  
9) Let user set Reminders
10) Let user Assign Tasks to other users
11) Allow for multiple projects
12) Track total time online
13) Restrict task deletion
14) User can split tasks in sub tasks
15) Let user set agile/waterfall plan


------------------------------------------------------------------------USE-CASE-8------------------------------------------------------------------------

## Use Case Description

Product Name: Task Managerinator
Problem Statement: The project allows users to manage a set of tasks and be able to collaborate and share tasks with other users.

Use Case Name: Real-Time notification.
Date: 4 April, 2021

## Summary:

The user should get real-time notifications of deadlines, reminders, and tasks added by their group leader. It should also notify user about tasks completed by other members in the group and Notify users if they are added to a new group project. It will also display the messages sent by other users in the inbox as notifications.

## Actors:

1. Customers/User.
2. Clock.
3. System Software.

## Preconditions:

Precondition 1: The deadlines for the task, the date and time, must be set.
Precondition 2: Group leader must add the task, deadline, and add members working on the task.
Precondition 3: The user must send an invite to other users for collaboration.
Precondition 4: The completed task must be marked done by the worker.
Precondition 5: The user should send the message to be delivered through internal messaging service.

## Triggers:

1. When a deadline for a task is with in 24 hours.
2. When a new task or project is created by the group leader.
3. When deadlines are set/altered for a particular task.
4. When a task is marked as completed.
5. When a user receive an invite to join a group project.
6. When the user receives a private/group message through internal messaging service. 

## Primary Sequence:

1. Step 1: When a message, private/system message, is received in the inbox, push the message as a notification on the systems the user has the account opened.

## Primary Postconditions:

Postcondition 1: It will show the notifications across all devices.
Postcondition 2: The notification would be stored in the inbox within the users account.

## Alternate Sequence:

NO ALTERNATE SEQUENCE FOR THIS TASK SET.


------------------------------------------------------------------------USE-CASE-9------------------------------------------------------------------------

## Use Case Description

Product Name: Task Managerinator
Problem Statement: The project allows users to manage a set of tasks and be able to collaborate and share tasks with other users.

Use Case Name: Let user set reminders.
Date: 4 April, 2021

## Summary:

The user should be able to set reminders for different tasks assigned by setting date and time as the reminder and receive notification reminders.

## Actors:

1. Customer/User.
2. Clock.
3. System Software.

## Preconditions:

Precondition 1: The date and time for the task should be set.
Precondition 2: The task to be reminded should not be marked as completed.

## Triggers:

1. When the date and time set for a task matches the current time.

## Primary Sequence:

1. Check if the present time matches the date and time of any assigned tasks.
2. Check if the matched task has been completed.
3. If not completed, ring an alarm tone with notification for the user.
4. Add new reminder by checking the time and date to be appropriate - reminder should have a future time. 

## Primary Postconditions:

Postcondition 1: Ring the alarm for 1 minute.
Postcondition 2: Wait for the user response to the alarm - turn off alarm or mark as completed.
Postcondition 3: Look for a different reminder by checking date and time and repeat the process.  

## Alternate Sequence:

NO ALTERNATE SEQUENCE FOR THIS TASK SET.

------------------------------------------------------------------------USE-CASE-10------------------------------------------------------------------------

## Use Case Description

Product Name: Task Managerinator
Problem Statement: The project allows users to manage a set of tasks and be able to collaborate and share tasks with other users.

Use Case Name: Let user assign tasks to other users.
Date: 4 April, 2021

## Summary:

The user should be able to assign tasks to different users and groups with in the project. Other users should accept the invitation to join the group before the user/admin can set tasks for other members of the group. 

## Actors:

1. Customer/User.
2. Clock.

## Preconditions:

Precondition 1: The user should be the admin of the group or have the permission to change or add tasks.
Precondition 2: Other group members should accept the invitation to collaborate in group.
Precondition 3: The added task should be with in the group project.
Precondition 4: The user/users must be selected to assign the task.

## Triggers:

1. When user with permission adds a new task with other group members.
2. When user with permission changes attributes of a task which has other members working with in a group.

## Primary Sequence:

1. Check if the user has the permission to change or add tasks for other members.
2. Check if the other members are working with in the same group as the task being added or changed.
3. Allow user to add tasks for a group of users or other users as selected.
4. Check if the time and date are correct and do not correspond to a time in the past as a deadline.
5. Set priority for the task to be assigned and requirements to be fullfilled.
6. Set new tasks or change the deadlines/requirements for the preexisting tasks for other users.

## Primary Postconditions:

Postcondition 1: Set, add or change, task in the users dashboard who is assigned the task.
Postcondition 2: Notify user about the added task through notification.
Postcondition 3: Set reminders and priority as assigned by the leader or the user assigning the task.

## Alternate Sequence:

NO ALTERNATE SEQUENCE FOR THIS TASK SET.

------------------------------------------------------------------------USE-CASE-11------------------------------------------------------------------------

## Use Case Description

Product Name: Task Managerinator
Problem Statement: The project allows users to manage a set of tasks and be able to collaborate and share tasks with other users.

Use Case Name: Allow for multiple projects.
Date: 4 April, 2021

## Summary:

The user should be able to work on multiple different projects by setting separate reminders and deadlines. The projects can be personal or group projects and multiple projects can have the same deadline.

## Actors:

1. Customer/User.
2. Clock.
3. System Software.

## Preconditions:

Precondition 1: There should be atleast one non-empty project pre-defined. 
Precondition 2: There user should be logged in to create new projects.

## Triggers:

1. The user wants to create or work on multiple projects at the same time.
2. The user tries to create a new project when there are other predefined projects and tasks.
3. The user want to work on multiple group projects with a team.

## Primary Sequence:

1. The user creates a new project and sets Agile or Waterfall model to be implemented.
2. The user schedules tasks with deadlines and meetings.
3. System check if the date and time are valid and adds the new tasks to calendar.
4. The user enters the priority for each task.
5. The user can add more members to the project and send invitation to collaborate to other users.
6. The users sets permission level for other added members.
7. The user assigns tasks to other members as the project creator is the admin by default.

## Primary Postconditions:

Postcondition 1: Set new dates and times for newly added projects.
Postcondition 2: Set reminders for the new tasks within the new projects.
Postcondition 3: Send notification about the created project to its members.
Postcondition 4: Create a new tab on the dashboard with the new project.
Postcondition 5: Set priority accordingly as compared to other projects and their tasks.
Postcondition 6: Set deadlines on the central calendar with scheduled meetings and events.
Postcondition 7: Assign the tasks to others and generate progress reports.
Postcondition 8: Set Agile or Waterfall plans for the project.
Postcondition 9: Disable task deletion for members without permission.

## Alternate Sequence:

NO ALTERNATE SEQUENCE FOR THIS TASK SET.

------------------------------------------------------------------------USE-CASE-12------------------------------------------------------------------------



NON-FUNCTIONAL REQUIREMENTS:
1) The system shall be available 24 hours/day and be able to upgrade while it is running.
2) System shall authenticate the user to maintain security and privacy.
3) System shall display 10 tasks per page and download files within five seconds.

