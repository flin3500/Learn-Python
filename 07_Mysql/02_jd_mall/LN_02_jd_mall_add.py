from pymysql import *

class Jd(object):

	def __init__(self, password):
		self.conn = connect(host='localhost',port=3306,database='jing_dong',user='root',password=password,charset='utf8')
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

	def add_brand(self):
		brand_name = input("Input new brand name: ")
		sql = """insert into goods_brands (name) values("%s")""" % brand_name
		self.cur.execute(sql)
		self.conn.commit()

	@staticmethod
	def print_menu():
		print("-----Jd mall-----")
		print("1: show all product")
		print("2: show all category")
		print("3: show all brand")
		print("4: add brand")
		print("5: exit")
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
				self.add_brand()
			elif op == "5":
				exit()
			else:
				print("Wrong, Please enter again")



def main():
	password = input("Input password: ")
	jd = Jd(password)
	jd.run()


if __name__ == "__main__":
	main()