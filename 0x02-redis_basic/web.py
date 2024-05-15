#!/usr/bin/env python3
"""
Caching request module.
"""
import redis
import requests
from functools import wraps
from typing import Callable


def track_get_page(fn: Callable) -> Callable:
    """Decorator to track the number of calls to the get_page function and cache the responses."""
    @wraps(fn)
    def wrapper(url: str) -> str:
        """Wrapper that checks if the URL's data is cached.
        If cached, it returns the cached data.
        Otherwise, it makes an HTTP request, caches the response, and returns it."""
        client = redis.Redis()
        client.incr(f'count:{url}')
        cache_page = client.get(f'{url}')
        if cache_page:
            return cache_page.decode('utf-8')
        response = fn(url)
        client.set(f'{url}', response, ex=10)  # Set cache with an expiration of 10 seconds
        return response
    return wrapper


@track_get_page
def get_page(url: str) -> str:
    """Makes an HTTP request to a given URL and returns the response text."""
    response = requests.get(url)
    return response.text  # Removed print to ensure the function returns the response

if __name__ == "__main__":
    # Example usage
    print(get_page('http://slowwly.robertomurray.

