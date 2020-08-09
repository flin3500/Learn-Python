import re
import pymysql

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
    conn = pymysql.connect(host='localhost',port=3306,user='root',password='',database='stock_db',charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from info;")
    stock_info = cursor.fetchall()
    cursor.close()
    conn.close()

    tr_template = """<tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>
            <input type="button" value="Add" id="toAdd" name="toAdd" systemidvaule="000007">
        </td>
        </tr>
    """

    html = ""
    for line_info in stock_info:
        html += tr_template % (line_info[0],line_info[1],line_info[2],line_info[3],line_info[4],line_info[5],line_info[6],line_info[7])

    content = re.sub(r"\{%content%\}", html, content)

    return content

@route("/center.html")
def center():
    with open("templates/center.html") as f:
       content = f.read()

    conn = pymysql.connect(host='localhost',port=3306,user='root',password='',database='stock_db',charset='utf8')
    cs = conn.cursor()
    cs.execute("select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info from info as i inner join focus as f on i.id=f.info_id;")
    stock_infos = cs.fetchall()
    cs.close()
    conn.close()

    tr_template = """
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <a type="button" class="btn btn-default btn-xs" href="/update/300268.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> Change </a>
            </td>
            <td>
                <input type="button" value="Delete" id="toDel" name="toDel" systemidvaule="300268">
            </td>
        </tr>
    """

    html = ""
    for line_info in stock_infos:
        html += tr_template % (line_info[0],line_info[1],line_info[2],line_info[3],line_info[4],line_info[5],line_info[6])

    # content = re.sub(r"\{%content%\}", str(stock_infos), content)
    content = re.sub(r"\{%content%\}", html, content)

    return content



def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = environ['PATH_INFO']
    try:
        return URL_FUN_DICT[file_name]()
    except Exception as e:
        return "Have error %s" % str(e)