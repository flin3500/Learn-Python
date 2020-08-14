from LN_01_mongo_db import client

try:
	teachers = client.school.teacher.find({}).skip(0).limit(10)
	for one in teachers:
		print(one["_id"],one["name"])
	print("---------------------")
	names = client.school.teacher.distinct("name")
	for one in names:
		print(one)
	print("---------------------")
	teachers = client.school.teacher.find({}).sort([("name",-1)])
	for one in teachers:
		print(one["_id"],one["name"])
except Exception as e:
	print(e)