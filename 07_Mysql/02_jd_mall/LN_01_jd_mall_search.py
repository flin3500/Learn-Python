from pymysql import *

class Jd(object):

	def __init__(self, password):
		self.conn = connect(host='localhost',port=3306,database='jd_mall',user='root',password=password,charset='utf8')
		self.cur = self.conn.cursor()

	def __del__(self):
		self.cur.close()
		self.conn.close()

	def execute_sql(self,sql):
		self.cur.execute(sql)
		for temp in self.cur.fetchall():
			print(temp)

	def show_all_product(self):
		sql = "select * from goods;"
		self.execute_sql(sql)
		
	def show_all_category(self):
		sql = "select name from goods_cates;"
		self.execute_sql(sql)

	def show_all_brand(self):
		sql = "select name from goods_brands;"
		self.execute_sql(sql)

	@staticmethod
	def print_menu():
		print("-----Jd mall-----")
		print("1: show all product")
		print("2: show all category")
		print("3: show all brand")
		print("4: exit")
		op = input("Please input the num you want to do: ")
		return op

	def run(self):
		while True:
			op = self.print_menu()
			if op == "1":
				self.show_all_product()
			elif op == "2":
				self.show_all_category()
			elif op == "3":
				self.show_all_brand()
			elif op == "4":
				exit()
			else:
				print("Wrong, Please enter again")



def main():
	password = input("Input password: ")
	jd = Jd(password)
	jd.run()


if __name__ == "__main__":
	main()