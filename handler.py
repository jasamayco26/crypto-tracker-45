import json
import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


class CryptoAPIError(Exception):
    """Custom exception raised for unrecoverable API payload errors."""
    pass


def parse_ticker_payload(raw_payload: str) -> Dict[str, float]:
    """Parse raw API ticker JSON and extract valid asset prices safely.

    Handles edge cases such as malformed JSON, missing data fields,
    negative values, and non-numeric price data.
    """
    if not raw_payload or not isinstance(raw_payload, str):
        logger.warning("Received invalid or empty raw payload string")
        return {}

    try:
        payload_data = json.loads(raw_payload)
    except json.JSONDecodeError as err:
        logger.error(f"Failed to decode payload JSON: {err}")
        return {}

    if not isinstance(payload_data, dict):
        logger.error(f"Expected dict payload, got {type(payload_data).__name__}")
        return {}

    data_section = payload_data.get("data", payload_data)
    if not isinstance(data_section, dict):
        logger.error("Nested data section is not a dictionary")
        return {}

    clean_prices: Dict[str, float] = {}

    for ticker, val in data_section.items():
        if not isinstance(ticker, str) or not ticker.strip():
            continue

        symbol = ticker.strip().upper()
        try:
            price = float(val)
            if price < 0:
                logger.warning(f"Discarding negative price for asset {symbol}: {price}")
                continue
            clean_prices[symbol] = price
        except (ValueError, TypeError):
            logger.warning(f"Cannot convert price value '{val}' to float for {symbol}")
            continue

    return clean_prices
