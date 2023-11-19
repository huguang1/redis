import redis
import time


r = redis.Redis(host='localhost', port=6379)
a = time.time()
for i in range(8000000):
    r.set(str(i), ''.join([str(j) for j in range(i)]))
    if not i % 100:
        print(i)

r.close()
print(time.time()-a)

