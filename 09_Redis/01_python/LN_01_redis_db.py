import redis

pool = redis.ConnectionPool(
	host = "locahost",
	port = 6379,
	password = "redislin",
	db = 0,
	max_connections=20
)