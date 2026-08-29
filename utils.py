import time
import random
import logging
from functools import wraps
from typing import Any, Callable, Optional, Type, Tuple
import requests

logger = logging.getLogger(__name__)

def retry_network_operation(
    max_retries: int = 3,
    initial_delay: float = 1.0,
    max_delay: float = 30.0,
    backoff_factor: float = 2.0,
    exceptions: Tuple[Type[Exception], ...] = (requests.exceptions.RequestException, ConnectionError, TimeoutError)
) -> Callable:
    """Decorator to add retry logic to network operations.

    Uses exponential backoff with jitter to avoid thundering herd.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = initial_delay
            last_exception: Optional[Exception] = None
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(
                        f"Attempt {attempt} failed for {func.__name__}: {str(e)}"
                    )
                    if attempt == max_retries:
                        logger.error(
                            f"All {max_retries} retries exhausted for {func.__name__}"
                        )
                        break
                    # Exponential backoff with jitter
                    delay = min(delay * backoff_factor, max_delay)
                    jitter = random.uniform(0, delay * 0.1)
                    sleep_time = delay + jitter
                    logger.info(f"Retrying in {sleep_time:.2f} seconds")
                    time.sleep(sleep_time)
            if last_exception is not None:
                raise last_exception
            # Fallback, though shouldn't happen
            return None
        return wrapper
    return decorator

# Practical example for crypto tracker
@retry_network_operation(max_retries=5, initial_delay=0.5, max_delay=10.0)
def get_crypto_price(symbol: str) -> float:
    """Get current price for a crypto symbol with automatic retries."""
    # Simulate or real call
    url = f"https://api.example.com/v1/price?symbol={symbol}"
    resp = requests.get(url, timeout=5)
    resp.raise_for_status()
    data = resp.json()
    return data.get("price", 0.0)