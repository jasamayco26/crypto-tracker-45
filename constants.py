"""
Global configuration constants for crypto-tracker-45.
"""

# API endpoints
COINGECKO_API_BASE = "https://api.coingecko.com/api/v3"
BINANCE_API_BASE = "https://api.binance.com/api/v3"

# Supported cryptocurrency pairs
SUPPORTED_PAIRS = [
    "BTCUSDT",
    "ETHUSDT",
    "SOLUSDT",
    "ADAUSDT",
    "DOTUSDT"
]

# Default polling interval in seconds
DEFAULT_POLL_INTERVAL = 60

# Database configuration
DB_FILE_NAME = "crypto_tracker.db"
DB_TIMEOUT = 30.0

# HTTP request settings
REQUEST_TIMEOUT = 10
MAX_RETRIES = 3
RETRY_BACKOFF_FACTOR = 1.5
