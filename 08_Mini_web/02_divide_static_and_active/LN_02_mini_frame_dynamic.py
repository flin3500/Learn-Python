import  time

def login():
	return "Welcome to our website. Time: %s" % time.ctime()

def register():
	return "Reigister. Time: %s" % time.ctime()

def profile():
	return "This is your profile. Time: %s" % time.ctime()

def application(file_name):
	if file_name == "/login.py":
		return login()
	elif file_name == "/register.py":
		return register()
	elif file_name == "/profile.py":
		return profile()
	else:
		return "NOT FOUND"

	