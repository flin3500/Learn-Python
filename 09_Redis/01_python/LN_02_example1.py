from LN_01_redis_db import pool
import redis
import time

conn = redis.Redis(
	connection_pool=pool
)

conn.set("country", "Britain")
conn.set("city", "London")
city = conn.get("city").decode("utf-8")
print(city)
conn.expire("city", 5)
time.sleep(6)
city = conn.get("city").decode("utf-8")
print(city)

del conn