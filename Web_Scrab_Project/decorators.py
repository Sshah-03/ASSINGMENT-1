import asyncio
import json
import os
import time
from functools import wraps

CACHE_FILE = "cache.json"

def rate_limit(calls_per_second: int):
    interval = 1 / calls_per_second
    last_called = 0

    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            nonlocal last_called
            elapsed = time.time() - last_called
            if elapsed < interval:
                await asyncio.sleep(interval - elapsed)
            result = await func(*args, **kwargs)
            last_called = time.time()
            return result
        return wrapper
    return decorator

def cached(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        key = f"{func.__name__}:{args}:{kwargs}"

        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, "r") as f:
                cache_data = json.load(f)
        else:
            cache_data = {}

        if key in cache_data:
            print("Returning cached data...")
            return cache_data[key]

        result = await func(*args, **kwargs)
        cache_data[key] = result

        with open(CACHE_FILE, "w") as f:
            json.dump(cache_data, f)

        return result
    return wrapper
