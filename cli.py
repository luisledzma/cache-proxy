import uvicorn
from config import get_config
from app.cache import clear

def main():
    args = get_config()

    if args.clear_cache:
        clear()
        print("Cache cleared.")
        return

    uvicorn.run("app.main:app", host="0.0.0.0", port=args.port, reload=True)

if __name__ == "__main__":
    main()
