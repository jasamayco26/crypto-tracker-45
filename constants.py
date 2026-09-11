from enum import Enum
from typing import Dict, Final

class ExchangeLimits(Enum):
    MAX_RETRY_ATTEMPTS: int = 3
    CONNECTION_TIMEOUT: int = 10
    BATCH_SIZE: int = 50
    CACHE_TTL_SECONDS: int = 300

# Optimized symbol lookup for reduced memory footprint
SUPPORTED_ASSETS: Final[Dict[str, str]] = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "SOL": "solana",
    "ADA": "cardano",
    "DOT": "polkadot",
    "MATIC": "polygon",
    "LINK": "chainlink",
    "DOGE": "dogecoin"
}

# Performance tuning parameters for rate limiting
API_RATE_LIMIT_MS: int = 250
THREAD_POOL_WORKERS: int = 4

def get_cache_expiry() -> int:
    """Returns standard TTL for asset price data."""
    return ExchangeLimits.CACHE_TTL_SECONDS.value

def get_batch_size() -> int:
    """Returns the optimized request batch size."""
    return ExchangeLimits.BATCH_SIZE.value