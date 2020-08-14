from LN_01_mongo_db import client

try:
	client.school.teacher.update_many({},{"$set":{"role":["head teacher"]}})

	client.school.teacher.update_one({"name":"Vicky"},{"$set":{"sex":"female"}})

	client.school.teacher.update_one({"name":"Vicky"},{"$push":{"role":"math teacher"}})
except Exception as e:
	print(e)
