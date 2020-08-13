from LN_01_redis_db import pool
import redis
import random

conn = redis.Redis(
	connection_pool=pool
)

try:
	conn.flushall()
	conn.zadd("ballot",{"Jack":0,"Scott":0,"Lin":0,"Ben":0,"Vicky":0})
	names = ["Jack","Scott","Lin","Ben","Vicky"]
	for i in range(0,300):
		num = random.randint(0,4)
		name = names[num]
		conn.zincrby("ballot",1,name)
	result = conn.zrevrange("ballot",0,-1,"WITHSCORES")
	for one in result:
		print(one[0].decode("utf-8"),int(one[1]))
except Exception as e:
	print(e)
finally:
	del conn