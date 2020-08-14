from LN_01_mongo_db import client

try:
	client.school.teacher.insert_one({"name":"Lin"})
	client.school.teacher.insert_many([
		{"name":"Vicky"},
		{"name":"Will"}
	])
except Exception as e:
	print(e)