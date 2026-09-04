from typing import Dict, Any, Union

def format_currency(amount: float, currency: str = "USD") -> str:
    """Format a numeric amount as a currency string.

    Args:
        amount: The financial value to format.
        currency: The target currency symbol (e.g., USD, EUR).

    Returns:
        A formatted string representation of the currency.
    """
    if amount >= 1.0:
        return f"{currency} {amount:,.2f}"
    return f"{currency} {amount:,.6f}"

def calculate_percentage_change(old_price: float, new_price: float) -> float:
    """Calculate the percentage change between two price points.

    Args:
        old_price: The historical price.
        new_price: The current price.

    Returns:
        The percentage change as a float. Returns 0.0 if old_price is zero.
    """
    if old_price == 0.0:
        return 0.0
    return ((new_price - old_price) / old_price) * 100.0

def parse_ticker_data(data: Dict[str, Any]) -> Dict[str, Union[str, float]]:
    """Extract and normalize ticker information from an API response dictionary.

    Args:
        data: Raw payload from a cryptocurrency API.

    Returns:
        A dictionary containing normalized symbol, price, and volume.
    """
    symbol = str(data.get("symbol", "UNKNOWN")).upper()
    price = float(data.get("price", 0.0))
    volume = float(data.get("volume", 0.0))
    
    return {
        "symbol": symbol,
        "price": price,
        "volume": volume
    }