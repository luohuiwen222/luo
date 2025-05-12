#!/usr/bin/python3
import redis
pool = redis.ConnectionPool(host="192.168.74.66",port=6379,password="",decode_responses=True)
r = redis.Redis(connection_pool=pool)
for i in range(100000):
    r.set("k%d" % i,"v%d" % i)
    data=r.get("k%d" % i)
    print(data)
