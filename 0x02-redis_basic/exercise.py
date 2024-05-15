#!/usr/bin/env python3
"""Redis-based caching module"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of times a method is called"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Increments the call count each time the method is called"""
        k = method.__qualname__
        self._redis.incr(k)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs of a method"""
    inkey = method.__qualname__ + ":inputs"
    outkey = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Pushes method inputs and outputs to Redis lists"""
        self._redis.rpush(inkey, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(outkey, str(res))
        return res

    return wrapper


def replay(method: Callable) -> None:
    """Displays the history of calls to a method"""
    input_key = "{}:inputs".format(method.__qualname__)
    output_key = "{}:outputs".format(method.__qualname__)

    inputs = method.__self__._redis.lrange(input_key, 0, -1)
    outputs = method.__self__._redis.lrange(output_key, 0, -1)

    print("{} was called {} times:".format(method.__qualname__, len(inputs)))
    for inp, out in zip(inputs, outputs):
        print(
            "{}(*{}) -> {}".format(
                method.__qualname__, inp.decode("utf-8"), out.decode("utf-8")
            )
        )


class Cache:
    """Cache class using Redis for storage"""

    def __init__(self):
        """Initialize the Cache with a Redis connection and clear the database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in the cache and return a unique key"""
        key_x = str(uuid.uuid4())
        self._redis.set(key_x, data)
        return key_x

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        """Retrieve data from the cache and optionally apply a conversion function"""
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Retrieve data from the cache as a string"""
        return self.get(key, fn=str)

    def get_int(self, key: str) -> int:
        """Retrieve data from the cache as an integer"""
        return self.get(key, fn=int)

