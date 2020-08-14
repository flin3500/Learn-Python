from LN_01_mongo_db import client

try:
	teacher = client.school.teacher.find({})
	for one in teacher:
		print(one["_id"],one["name"])
	print("--------------------------")
	teacher = client.school.teacher.find_one({"name":"Lin"})
	print(teacher["_id"],teacher["name"])
except Exception as e:
	print(e)