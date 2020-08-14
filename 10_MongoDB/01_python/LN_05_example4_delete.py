from LN_01_mongo_db import client

try:
	client.school.teacher.delete_one({"name":"Vicky"})
	client.school.teacher.delete_many({})
except Exception as e:
	print(e)