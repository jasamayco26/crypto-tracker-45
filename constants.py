"""Constants for crypto data handling and API configuration."""

from typing import Dict, List

# API Endpoints and Base URLs
COINGECKO_BASE_URL: str = "https://api.coingecko.com/api/v3"
BINANCE_BASE_URL: str = "https://api.binance.com/api/v3"

# Request Configurations
DEFAULT_TIMEOUT_SECONDS: int = 10
MAX_RETRIES: int = 3
RETRY_BACKOFF_FACTOR: float = 0.5

# Cache Expiration Settings (in seconds)
PRICE_CACHE_TTL: int = 60
MARKET_CAP_CACHE_TTL: int = 300
OHLC_CACHE_TTL: int = 900

# Supported Fiat Currencies for Pairings
SUPPORTED_FIAT_CURRENCIES: List[str] = [
    "usd",
    "eur",
    "gbp",
    "jpy",
    "cad",
    "aud",
]

# Supported Crypto Symbols for Default Tracking
DEFAULT_TRACKED_SYMBOLS: List[str] = [
    "btc",
    "eth",
    "sol",
    "ada",
    "dot",
    "xrp",
]

# Standard API Error Messages
ERROR_MESSAGES: Dict[str, str] = {
    "rate_limit": "Rate limit exceeded. Please wait before retrying.",
    "network_error": "Failed to connect to cryptocurrency provider API.",
    "invalid_symbol": "Provided cryptocurrency symbol is not supported.",
    "timeout": "Request to cryptocurrency API timed out.",
}
