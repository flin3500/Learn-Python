from LN_03_redis_db import pool
from concurrent.futures import ThreadPoolExecutor
import redis
import random

users = set()
# create 1000 unique userid
while True:
	if len(users)==1000:
		break
	num = random.randint(10000,100000)
	users.add(num)

connection = redis.Redis(connection_pool=pool)

try:
	connection.flushall()
	connection.set("kill_total",50)
	connection.set("kill_num",0)
	connection.set("kill_flag",1)
	connection.expire("kill_flag",600)
except Exception as e:
	print(e)
finally:
	del connection


def buy():
	conn = redis.Redis(connection_pool=pool)
	pipeline = conn.pipeline()
	try:
		if conn.exists("kill_flag") == 1:
			pipeline.watch("kill_num","kill_user")
			total = int(pipeline.get("kill_total").decode("utf-8"))
			num = int(pipeline.get("kill_num").decode("utf-8"))
			if num < total:
				pipeline.multi()
				pipeline.incr("kill_num")
				user_id = users.pop()
				pipeline.rpush("kill_user",user_id)
				pipeline.execute()
	except Exception as e:
		print(e)
	finally:
		if "pipeline" in dir():
			pipeline.reset()
		del conn

excutor = ThreadPoolExecutor(200)
for i in range(0,1000):
	excutor.submit(buy())

print("Finish")