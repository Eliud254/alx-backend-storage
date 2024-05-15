#!/usr/bin/env python3
'''Expiring web cache and tracker
'''
import redis
import requests
from datetime import timedelta

def get_page(url: str) -> str:
    '''This tracks the number of accesses,
    and caches the result with an expiration time of 10 seconds.
    '''
    if url is None or len(url.strip()) == 0:
        return ''

    # Connect to Redis
    redis_store = redis.Redis()

    # Define Redis keys for result and request count
    res_key = 'result:{}'.format(url)
    req_key = 'count:{}'.format(url)

    # Check if the result is cached in Redis
    result = redis_store.get(res_key)
    if result is not None:
        redis_store.incr(req_key)
        return result.decode('utf-8')

    result = requests.get(url).content.decode('utf-8')

    redis_store.setex(res_key, timedelta(seconds=10), result)

    redis_store.incr(req_key)

    return result

if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    print(get_page(url))
