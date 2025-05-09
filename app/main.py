from fastapi import FastAPI, Request, Response
from app.proxy import fetch_from_origin, fetch_from_cache
from config import get_config

args = get_config()
app = FastAPI()
origin = args.origin

@app.get("/{path:path}")
async def proxy(path: str, request: Request):
    cached = fetch_from_cache(origin, path)
    if cached:
        data, headers = cached
        headers["X-Cache"] = "HIT"
        return Response(content=data, headers=headers)

    data, headers = fetch_from_origin(origin, path)
    headers["X-Cache"] = "MISS"
    return Response(content=data, headers=headers)