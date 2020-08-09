URL_FUN_DICT = dict()

def route(url):
    def set_func(func):
        URL_FUN_DICT[url] = func
        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func

@route("/index.html")
def index():
    with open("templates/index.html") as f:
       content = f.read()
    return content

@route("/center.html")
def center():
    with open("templates/center.html") as f:
       content = f.read()
    return content



def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = environ['PATH_INFO']
    try:
        return URL_FUN_DICT[file_name]()
    except Exception as e:
        return "Have error %s" % str(e)