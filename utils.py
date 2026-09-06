from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)

def format_currency(amount: float, symbol: str = 'USD') -> str:
    """Formats a numeric crypto value into a localized currency string."""
    try:
        return f"{amount:,.2f} {symbol}"
    except ValueError as e:
        logger.error(f"Format error: {e}")
        return "0.00"

def calculate_profit_margin(buy_price: float, current_price: float) -> float:
    """Calculates percentage difference between purchase and current price."""
    if buy_price <= 0:
        return 0.0
    margin = ((current_price - buy_price) / buy_price) * 100
    return round(margin, 2)

def sanitize_ticker(ticker: str) -> str:
    """Normalizes crypto ticker symbols to uppercase."""
    return str(ticker).strip().upper()

def get_asset_info(data: Dict[str, Any], key: str) -> Optional[Any]:
    """Safe lookup for nested crypto data objects."""
    return data.get(key) if isinstance(data, dict) else None