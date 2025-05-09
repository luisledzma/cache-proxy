import argparse

def get_config():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=3000, help="Port for the proxy server")
    parser.add_argument("--origin", type=str, help="Origin server base URL")
    parser.add_argument("--clear-cache", action="store_true", help="Clear the cache and exit")
    return parser.parse_args()
