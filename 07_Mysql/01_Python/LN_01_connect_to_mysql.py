from pymysql import *

def main():
	password = input("Input password: ")
	conn = connect(host='localhost',port=3306,database='xx',user='root',password=password,charset='utf8')
	cur = conn.cursor()

	cur.execute("select * from goods;")
	print(cur.fetchall())
	cur.close()
	conn.close()


if __name__ == "__main__":
	main()