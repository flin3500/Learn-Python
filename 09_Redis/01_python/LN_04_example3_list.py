from LN_01_redis_db import pool
import redis

conn = redis.Redis(
	connection_pool=pool
)

try:
	conn.flushall()
	conn.rpush("name","lin","vicky","will","scott")
	conn.lpop("name")
	result = conn.lrange("name", 0, -1)
	for one in result:
		print(one.decode("utf-8"))
except Exception as e:
	print(e)
finally:
	del conn