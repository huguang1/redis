import redis


r = redis.Redis(host='localhost', port=6379)

for i in range(10000000):
    r.set(str(i), str(i)*1000000)
    if not i % 100:
        print(i)

r.close()




