from LN_01_redis_db import pool
import redis

conn = redis.Redis(
	connection_pool=pool
)

try:
	conn.flushall()
	dict_set = {"name":"scott","sex":"male","city":"London"}
	conn.hmset("9527",dict_set)
	conn.hset("9527","age","18")
	conn.hdel("9527","age")
	result = conn.hexists("9527", "name")
	print(result)
	result = conn.hgetall("9527")
	for one in result:
		print(one.decode("utf-8"), result[one].decode("utf-8"))
except Exception as e:
	print(e)
finally:
	del conn