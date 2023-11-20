from rediscluster import RedisCluster, ClusterConnectionPool
import time


startup_nodes = [
    {'host': '127.0.0.1', 'port': 6379},
    {'host': '127.0.0.1', 'port': 6380},
    {'host': '127.0.0.1', 'port': 6381}
    ]
# 构建连接池
pool = ClusterConnectionPool(startup_nodes=startup_nodes)

# 创建redis集群客户端
redis_client = RedisCluster(connection_pool=pool)

# 数据写入测试
for i in range(100000000):
    redis_client.set(str(i), str(i))






