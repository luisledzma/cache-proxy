cache = {}

def get(url: str):
    return cache.get(url)

def set(url: str, data: bytes, headers: dict):
    cache[url] = (data, headers)

def clear():
    cache.clear()