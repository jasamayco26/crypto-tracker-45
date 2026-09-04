import asyncio
import time
from typing import Dict, List, Any, Callable, Awaitable


class PriceAggregator:
    """Aggregates crypto ticker prices with TTL caching for high throughput."""

    def __init__(self, cache_ttl_seconds: float = 2.0):
        self.cache_ttl = cache_ttl_seconds
        self._cache: Dict[str, Dict[str, Any]] = {}

    def _is_cache_valid(self, symbol: str) -> bool:
        if symbol not in self._cache:
            return False
        return (time.time() - self._cache[symbol]["timestamp"]) < self.cache_ttl

    async def fetch_symbol_price(
        self, 
        symbol: str, 
        raw_fetcher: Callable[[str], Awaitable[Dict[str, Any]]]
    ) -> Dict[str, Any]:
        """Fetch symbol price using local cache to minimize redundant external API calls."""
        symbol_upper = symbol.upper()
        if self._is_cache_valid(symbol_upper):
            return self._cache[symbol_upper]["data"]

        price_data = await raw_fetcher(symbol_upper)
        self._cache[symbol_upper] = {
            "timestamp": time.time(),
            "data": price_data
        }
        return price_data

    async def batch_fetch_prices(
        self, 
        symbols: List[str], 
        raw_fetcher: Callable[[str], Awaitable[Dict[str, Any]]]
    ) -> Dict[str, Dict[str, Any]]:
        """Batch process ticker price requests concurrently using asyncio."""
        tasks = [self.fetch_symbol_price(symbol, raw_fetcher) for symbol in symbols]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        output = {}
        for symbol, result in zip(symbols, results):
            if not isinstance(result, Exception):
                output[symbol.upper()] = result
        return output

    def clear_expired_cache(self) -> int:
        """Purge stale cache entries to free up memory."""
        now = time.time()
        expired_keys = [
            key for key, entry in self._cache.items()
            if (now - entry["timestamp"]) >= self.cache_ttl
        ]
        for key in expired_keys:
            del self._cache[key]
        return len(expired_keys)
