from LN_01_redis_db import pool
import redis

conn = redis.Redis(
	connection_pool=pool
)

try:
	conn.delete("country")
	conn.mset({"country":"German", "city":"Berlin"})
	result = conn.mget("country", "city")
	for one in result:
		print(one.decode("utf-8")) 
except Exception as e:
	print(e)
finally:
	del conn