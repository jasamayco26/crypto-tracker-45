from typing import Union, Optional

def validate_ticker(ticker: str) -> bool:
    """
    Check if the provided ticker symbol follows crypto market standards.

    Args:
        ticker: The asset symbol (e.g., 'BTC', 'ETH').

    Returns:
        bool: True if valid, False otherwise.
    """
    if not isinstance(ticker, str) or not (2 <= len(ticker) <= 10):
        return False
    return ticker.isalnum()

def validate_price(price: Union[int, float]) -> bool:
    """
    Ensure the price is a positive numerical value.

    Args:
        price: The numeric price of the asset.

    Returns:
        bool: True if price is positive, False otherwise.
    """
    if not isinstance(price, (int, float)):
        return False
    return price > 0

def sanitize_input(value: Optional[str]) -> str:
    """
    Clean string input by removing whitespace and converting to uppercase.

    Args:
        value: The raw user input string.

    Returns:
        str: The sanitized ticker string.
    """
    if value is None:
        return ""
    return value.strip().upper()