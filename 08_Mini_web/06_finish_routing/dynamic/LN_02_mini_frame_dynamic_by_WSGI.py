def index():
    with open("templates/index.html") as f:
       content = f.read()
    return content

def center():
    with open("templates/center.html") as f:
       content = f.read()
    return content

URL_FUN_DICT = {
    "/index.py": index,
    "/center.py": center

}


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = environ['PATH_INFO']

    function = URL_FUN_DICT[file_name]
    return function()