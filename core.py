import functools
import time
from typing import Dict, Any

# Local cache for ticker data to avoid redundant API hits
_CACHE: Dict[str, Dict[str, Any]] = {}
_TTL = 30  # seconds

@functools.lru_cache(maxsize=128)
def get_cached_price(symbol: str) -> float:
    """Fetches price with basic caching mechanism."""
    # Simulate network latency
    time.sleep(0.1)
    return 42000.0 if symbol == "BTC" else 2500.0

def batch_process_tickers(symbols: list[str]) -> Dict[str, float]:
    """
    Performance optimization via result memoization
    and dictionary comprehension for bulk retrieval.
    """
    return {symbol: get_cached_price(symbol) for symbol in symbols}

def clear_stale_cache():
    """Force cache refresh for ticker data."""
    get_cached_price.cache_clear()

if __name__ == "__main__":
    data = batch_process_tickers(["BTC", "ETH", "BTC"])
    print(f"Processed prices: {data}")