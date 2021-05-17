from app.models import User

def new_user():        # Creating a new user
	user = User(username = "Test", email = "test@gmail.com", password = "unittest")
	return user

def test_new_user(new_user):        # Using assert to check if the data is same
	assert new_user.username == 'Test'
	assert new_user.email == 'test@gmail.com'
	assert new_user.password == 'unittest'

def new_user_1():        # Creating a new user
	user = User(username = "Prof. Rojas", email = "professor.rojas@gmail.com", password = "Prof_Rojas")
	return user

def test_new_user_1(new_user_1):        # Using assert to check if the data matches
	assert new_user_1.username == 'Prof. Rojas'
	assert new_user_1.email == 'professor.rojas@gmail.com'
	assert new_user_1.password == 'Prof_Rojas'

def run_user_test():        # Function to run all the tests and print if it passes
	print ('Running Test 1')
	test_new_user(new_user())
	print ('Test 1 Passed')

	print ('Running Test 2')
	test_new_user_1(new_user_1())
	print ('Test 2 Passed')

run_user_test()
