import redis

pool = redis.ConnectionPool(host='localhost', port=6379)
redis = redis.Redis(connection_pool=pool, decode_responses=True)
pipe = redis.pipeline()


for i in range(50000000):
    pipe.set(str(i), str(i))
    if not i % 1000:
        pipe.execute()
        print(i)






