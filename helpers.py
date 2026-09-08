"""Utility helper functions for crypto price and market data manipulation."""

from typing import Dict, Any, Union, Optional


def format_currency(value: Union[int, float], symbol: str = "$") -> str:
    """Format a numeric value as a currency string with appropriate precision."""
    if value is None:
        return f"{symbol}0.00"
    
    abs_val = abs(value)
    if abs_val >= 1.0:
        return f"{symbol}{value:,.2f}"
    elif abs_val >= 0.0001:
        return f"{symbol}{value:,.6f}"
    else:
        return f"{symbol}{value:,.8f}"


def calculate_price_change(current_price: float, previous_price: float) -> Dict[str, Any]:
    """Calculate absolute and percentage price changes between two points."""
    if previous_price <= 0:
        return {"change": 0.0, "percentage": 0.0, "direction": "neutral"}
    
    diff = current_price - previous_price
    pct = (diff / previous_price) * 100.0
    
    if diff > 0:
        direction = "up"
    elif diff < 0:
        direction = "down"
    else:
        direction = "neutral"
        
    return {
        "change": round(diff, 8),
        "percentage": round(pct, 2),
        "direction": direction
    }


def truncate_address(address: str, prefix_len: int = 6, suffix_len: int = 4) -> str:
    """Truncate a crypto wallet address for compact display."""
    if not address or len(address) <= (prefix_len + suffix_len):
        return address or ""
    return f"{address[:prefix_len]}...{address[-suffix_len:]}"


def normalize_ticker(symbol: str) -> str:
    """Normalize market ticker symbol to uppercase standard format."""
    if not symbol:
        return ""
    return symbol.strip().upper().replace("-", "").replace("/", "")
