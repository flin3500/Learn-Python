import re
import pymysql
import urllib.parse
import logging

URL_FUN_DICT = dict()

def route(url):
    def set_func(func):
        URL_FUN_DICT[url] = func
        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func

@route(r"/index.html")
def index(reg):
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
            <input type="button" value="Add" id="toAdd" name="toAdd" systemidvaule="%s">
        </td>
        </tr>
    """

    html = ""
    for line_info in stock_info:
        html += tr_template % (line_info[0],line_info[1],line_info[2],line_info[3],line_info[4],line_info[5],line_info[6],line_info[7], line_info[1])

    content = re.sub(r"\{%content%\}", html, content)

    return content

@route(r"/center.html")
def center(reg):
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
                <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> Change </a>
            </td>
            <td>
                <input type="button" value="Delete" id="toDel" name="toDel" systemidvaule="%s">
            </td>
        </tr>
    """

    html = ""
    for line_info in stock_infos:
        html += tr_template % (line_info[0],line_info[1],line_info[2],line_info[3],line_info[4],line_info[5],line_info[6], line_info[0],line_info[0])

    # content = re.sub(r"\{%content%\}", str(stock_infos), content)
    content = re.sub(r"\{%content%\}", html, content)

    return content

@route(r"/add/(\d+)\.html")
def add_focus(reg):
    stock_code = reg.group(1)
    conn = pymysql.connect(host='localhost',port=3306,user='root',password='',database='stock_db',charset='utf8')
    cursor = conn.cursor()
    sql = """select * from info where code = %s;"""
    cursor.execute(sql, (stock_code,))
    if not cursor.fetchone():
        cursor.close()
        conn.close()
        return "no this stock"
    sql = """select * from info as i inner join focus as f on i.id=f.info_id where i.code=%s;"""
    cursor.execute(sql, (stock_code,))
    if cursor.fetchone():
        cursor.close()
        conn.close()
        return "already in the list"
    sql = """insert into focus (info_id) select id from info where code=%s;"""
    cursor.execute(sql, (stock_code,))
    conn.commit()
    cursor.close()
    conn.close()

    return "Add succuess"


@route(r"/del/(\d+)\.html")
def del_focus(reg):
    stock_code = reg.group(1)
    conn = pymysql.connect(host='localhost',port=3306,user='root',password='',database='stock_db',charset='utf8')
    cursor = conn.cursor()
    sql = """select * from info where code = %s;"""
    cursor.execute(sql, (stock_code,))
    if not cursor.fetchone():
        cursor.close()
        conn.close()
        return "no this stock"
    sql = """select * from info as i inner join focus as f on i.id=f.info_id where i.code=%s;"""
    cursor.execute(sql, (stock_code,))
    if not cursor.fetchone():
        cursor.close()
        conn.close()
        return "not in the list"
    sql = """delete from focus where info_id = (select id from info where code=%s);"""
    cursor.execute(sql, (stock_code,))
    conn.commit()
    cursor.close()
    conn.close()

    return "Del succuess"


@route(r"/update/(\d+)\.html")
def show_update(reg):
    stock_code = reg.group(1)
    with open("templates/update.html") as f:
       content = f.read()

    conn = pymysql.connect(host='localhost',port=3306,user='root',password='',database='stock_db',charset='utf8')
    cursor = conn.cursor()

    sql = """select f.note_info from focus as f inner join info as i on i.id=f.info_id where i.code=%s;"""
    cursor.execute(sql, (stock_code,))
    note_info = cursor.fetchone()[0]
    
    cursor.close()
    conn.close()

    content = re.sub(r"\{\%note_info\%}", note_info, content)
    content = re.sub(r"\{\%code\%}", stock_code, content)

    return content


@route(r"/update/(\d+)/(.*)\.html")
def update(reg):
    stock_code = reg.group(1)
    comment = reg.group(2)
    comment = urllib.parse.unquote(comment)


    conn = pymysql.connect(host='localhost',port=3306,user='root',password='',database='stock_db',charset='utf8')
    cursor = conn.cursor()

    sql = """update focus set note_info=%s where info_id = (select id from info where code=%s);"""
    cursor.execute(sql, (comment,stock_code))
    conn.commit()

    cursor.close()
    conn.close()

    return "Update succuess"


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = environ['PATH_INFO']

    logging.basicConfig(level=logging.INFO,  
                    filename='./log.txt',  
                    filemode='w',  
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  

    logging.info("The url is %s" % file_name)
    try:
        for url, func in URL_FUN_DICT.items():
            reg = re.match(url, file_name)
            if reg:
                return func(reg)
        else:
            logging.warning("no this url_fun")
            return "no func in the url %s" % file_name
    except Exception as e:
        return "Have error %s" % str(e)