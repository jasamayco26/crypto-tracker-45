import time
import requests
from typing import Dict, Any, List, Optional
class CryptoCore:
    """Core module for crypto tracking with built-in network retry logic."""
    def __init__(self, base_url: str = "https://api.coingecko.com/api/v3"):
        self.base_url = base_url
        # Use session for persistent connections and better performance
        self.session = requests.Session()
    def _make_request(self, endpoint: str, params: Optional[Dict[str, str]] = None, max_retries: int = 5, backoff_factor: float = 0.5) -> Dict[str, Any]:
        """Execute network request with retry on transient failures."""
        url = f"{self.base_url}/{endpoint}"
        params = params or {}
        last_exception: Optional[Exception] = None
        for attempt in range(max_retries):
            try:
                response = self.session.get(url, params=params, timeout=15)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as exc:
                last_exception = exc
                if attempt < max_retries - 1:
                    # Exponential backoff to avoid overwhelming the server
                    sleep_duration = backoff_factor * (2 ** attempt)
                    time.sleep(sleep_duration)
        # All retries exhausted
        raise RuntimeError(f"Failed after {max_retries} attempts: {last_exception}") from last_exception
    def get_simple_price(self, coin_ids: List[str], vs_currencies: Optional[List[str]] = None) -> Dict[str, Any]:
        """Retrieve prices using the retry protected request method."""
        if vs_currencies is None:
            vs_currencies = ["usd"]
        params = {
            "ids": ",".join(coin_ids),
            "vs_currencies": ",".join(vs_currencies)
        }
        return self._make_request("simple/price", params)
    def get_market_data(self, coin_id: str) -> Dict[str, Any]:
        """Get market chart data with automatic retries for network issues."""
        endpoint = f"coins/{coin_id}/market_chart"
        params = {"vs_currency": "usd", "days": "1"}
        return self._make_request(endpoint, params)
def track_crypto_prices(coins: List[str]) -> Dict[str, float]:
    """High level function to track prices for given crypto coins."""
    core = CryptoCore()
    try:
        price_data = core.get_simple_price(coins)
        tracked = {}
        for coin in coins:
            if coin in price_data and "usd" in price_data[coin]:
                tracked[coin] = price_data[coin]["usd"]
            else:
                tracked[coin] = 0.0
        return tracked
    except Exception as e:
        # Log error but return defaults to keep app running
        print(f"Tracking failed: {e}")
        return {coin: 0.0 for coin in coins}
