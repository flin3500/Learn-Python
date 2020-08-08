def index():
	return "This is index"

def login():
	return "This is login"




def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = environ['PATH_INFO']
    if file_name == "/index.py":
    	return index()
    elif file_name == "/login.py":
    	return login()
    else:
    	return 'Hello World!'