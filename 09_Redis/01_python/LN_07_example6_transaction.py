from LN_01_redis_db import pool
import redis

conn = redis.Redis(
	connection_pool=pool
)

try:
	conn.flushall()
	dict_set = {"name":"scott","sex":"male","city":"London"}
	conn.hmset("9527",dict_set)


	pipeline = conn.pipeline()
	pipeline.watch("9527")
	pipeline.multi()
	pipeline.hset("9527", "name", "jack")
	pipeline.hset("9527","age","18")
	pipeline.execute()


except Exception as e:
	print(e)
finally:
	if "pipeline" in dir():
		pipeline.reset()
	del conn