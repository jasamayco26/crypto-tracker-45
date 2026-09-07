import requests
from requests.exceptions import RequestException, Timeout

class CryptoDataHandler:
    """Handles fetching and processing cryptocurrency market data."""

    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url
        self.timeout = timeout

    def fetch_price(self, symbol: str) -> float:
        """Fetches price with robust error handling for API reliability."""
        url = f"{self.base_url}/price/{symbol}"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            if 'price' not in data:
                raise ValueError(f"Invalid data structure for {symbol}")
                
            return float(data['price'])

        except Timeout:
            print(f"Request timed out for {symbol}")
            return 0.0
        except RequestException as e:
            print(f"Network error fetching {symbol}: {e}")
            return 0.0
        except (ValueError, KeyError) as e:
            print(f"Data parsing error for {symbol}: {e}")
            return 0.0
        except Exception as e:
            print(f"Unexpected error for {symbol}: {e}")
            return 0.0

    def get_market_status(self) -> bool:
        """Checks if the remote crypto exchange API is healthy."""
        try:
            resp = requests.head(self.base_url, timeout=5)
            return resp.status_code == 200
        except RequestException:
            return False