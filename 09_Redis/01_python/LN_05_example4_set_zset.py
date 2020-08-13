from LN_01_redis_db import pool
import redis

conn = redis.Redis(
	connection_pool=pool
)

try:
	conn.flushall()
	conn.sadd("employee", 8001, 8002, 8003)
	conn.srem("employee", 8002)
	result = conn.smembers("employee")
	for one in result:
		print(one.decode("utf-8"))

	conn.zadd("keyword", {"Jack": 0, "Mask": 0, "Berg": 0})
	conn.zincrby("keyword",10,"Jack")
	result=conn.zrevrange("keyword",0,-1)
	for one in result:
		print(one.decode("utf-8"))
except Exception as e:
	print(e)
finally:
	del conn