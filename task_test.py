from app.models import Tasks

def new_task():        # Creating a new user
	task = Tasks(task = 'Milestone 2', priority = '1', project = 'CMPE131', user = 'prof_rojas', completed = False)
	return task

def test_new_task(new_task):        # Using assert to check if the data matches
	assert new_task.task == 'Milestone 2'
	assert new_task.priority == '1'
	assert new_task.project == 'CMPE131'
	assert new_task.user == 'prof_rojas'
	assert new_task.completed == False

def new_task_1():        # Creating a new user
	task = Tasks(task = 'Milestone 3', priority = '3', project = 'CMPE131group4', user = 'team four', completed = True)
	return task

def test_new_task_1(new_task_1):        # Using assert to check if the data matches
	assert new_task_1.task == 'Milestone 3'
	assert new_task_1.priority == '3'
	assert new_task_1.project == 'CMPE131group4'
	assert new_task_1.user == 'team four'
	assert new_task_1.completed == True

def run_task_test():        # Function to run all the tests and print if it passes
	print ('Running Test 1')
	test_new_task(new_task())
	print ('Test 1 Passed')

	print ('Running Test 2')
	test_new_task_1(new_task_1())
	print ('Test 2 Passed')

run_task_test()
