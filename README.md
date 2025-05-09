# Caching Proxy Server (Python + FastAPI)

A lightweight caching proxy server that caches responses from a specified origin server. Built with FastAPI and Uvicorn.

---

## Features

- Forwards HTTP requests to a given origin server.
- Caches responses in memory.
- Adds `X-Cache: HIT` or `X-Cache: MISS` header.
- Clears cache with a CLI command.

---

## Project Structure

```
caching-proxy/
│
├── app/
│   ├── __init__.py
│   ├── proxy.py            # Logic to fetch from origin/cache
│   └── cache.py            # In-memory cache management
│
├── config.py               # CLI argument parser
├── cli.py                  # Entry point for running or clearing cache
├── requirements.txt        # Dependencies
└── README.md
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/caching-proxy.git
cd caching-proxy
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install fastapi uvicorn requests
```

### 4. Run the server

```bash
python3 cli.py --port 3000 --origin http://dummyjson.com
```

This starts the proxy server on `http://localhost:3000` and forwards requests to `http://dummyjson.com`.

---

## Example Usage

### Forward a request:

```bash
curl -i http://localhost:3000/products
```

- On first request: `X-Cache: MISS`
- On repeat request: `X-Cache: HIT`

---

## Clear the Cache

```bash
python3 cli.py --clear-cache
```

This will clear the in-memory cache.

---

## Test Endpoints

Try visiting these URLs via browser or `curl`:

- http://localhost:3000/products
- http://localhost:3000/products/1
- http://localhost:3000/users

---

## Notes

- The cache is stored in memory and resets when the server restarts.
- For persistent or distributed caching, consider Redis or a file-based solution.
- This project is intended for learning purposes and local experimentation.

---

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Requests

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---
