import requests
from app.cache import get, set

def fetch_from_origin(origin: str, path: str):
    url = f"{origin.rstrip('/')}/{path.lstrip('/')}"
    response = requests.get(url)
    set(url, response.content, dict(response.headers))
    return response.content, response.headers

def fetch_from_cache(origin: str, path: str):
    url = f"{origin.rstrip('/')}/{path.lstrip('/')}"
    return get(url)