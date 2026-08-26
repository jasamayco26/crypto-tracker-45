import time
from functools import lru_cache
from typing import Dict, List

class CryptoCore:
    """Core module for crypto tracker with performance optimizations."""

    def __init__(self, cache_ttl: int = 60):
        self.price_cache: Dict[str, tuple] = {}
        self.cache_ttl = cache_ttl

    @lru_cache(maxsize=256)
    def _fetch_price(self, symbol: str) -> float:
        # Simulated expensive API call for price fetching
        time.sleep(0.05)  # Representing network latency
        mock_prices = {
            'BTC': 65000.0,
            'ETH': 3200.0,
            'SOL': 145.0,
            'ADA': 0.45,
            'XRP': 0.52
        }
        return mock_prices.get(symbol.upper(), 0.0)

    def get_price(self, symbol: str) -> float:
        """Get price with TTL cache for performance."""
        current_time = time.time()
        if symbol in self.price_cache:
            cached_time, cached_price = self.price_cache[symbol]
            if current_time - cached_time < self.cache_ttl:
                return cached_price
        price = self._fetch_price(symbol)
        self.price_cache[symbol] = (current_time, price)
        return price

    def get_multiple_prices(self, symbols: List[str]) -> Dict[str, float]:
        """Optimized batch fetch using cache and set for uniqueness."""
        unique_symbols = set(symbol.upper() for symbol in symbols)
        prices = {}
        for symbol in unique_symbols:
            prices[symbol] = self.get_price(symbol)
        return prices

    def calculate_total_value(self, portfolio: Dict[str, float]) -> float:
        """Calculate portfolio value efficiently using generator expression."""
        return sum(
            self.get_price(symbol) * amount 
            for symbol, amount in portfolio.items()
        )

    def clear_expired_cache(self) -> int:
        """Remove expired entries to manage memory."""
        current_time = time.time()
        expired = [
            sym for sym, (ts, _) in self.price_cache.items()
            if current_time - ts >= self.cache_ttl
        ]
        for sym in expired:
            del self.price_cache[sym]
        return len(expired)