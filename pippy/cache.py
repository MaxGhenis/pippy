import json
from pathlib import Path
from datetime import datetime, timedelta

CACHE_DIR = Path.home() / ".pippy_cache"


def cache_response(key, data, expiry_hours=24):
    CACHE_DIR.mkdir(exist_ok=True)
    cache_file = CACHE_DIR / f"{key}.json"
    with cache_file.open("w") as f:
        json.dump(
            {
                "data": data,
                "expiry": (
                    datetime.now() + timedelta(hours=expiry_hours)
                ).isoformat(),
            },
            f,
        )


def get_cached_response(key):
    cache_file = CACHE_DIR / f"{key}.json"
    if cache_file.exists():
        with cache_file.open("r") as f:
            cached = json.load(f)
        if datetime.now() < datetime.fromisoformat(cached["expiry"]):
            return cached["data"]
    return None
