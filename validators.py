import re
from typing import Dict, Any, Union

class ValidationError(Exception):
    """Custom exception raised when validation fails."""
    pass

def validate_ticker(ticker: str) -> str:
    """Validate and normalize a cryptocurrency ticker symbol."""
    if not isinstance(ticker, str):
        raise ValidationError("Ticker must be a string")
    cleaned = ticker.strip().upper()
    if not re.match(r"^[A-Z0-9]{2,10}$", cleaned):
        raise ValidationError(f"Invalid ticker format: {ticker}")
    return cleaned

def validate_price(price: Union[int, float, str]) -> float:
    """Validate and convert price to a positive float."""
    try:
        val = float(price)
    except (ValueError, TypeError):
        raise ValidationError(f"Invalid price value: {price}")
    if val <= 0:
        raise ValidationError("Price must be greater than zero")
    return val

def validate_api_response(data: Dict[str, Any]) -> Dict[str, Any]:
    """Validate API payload structure and data integrity."""
    if not isinstance(data, dict):
        raise ValidationError("API response must be a dictionary")
    if "status" in data and data["status"] == "error":
        msg = data.get("message", "Unknown API error")
        raise ValidationError(f"API returned error: {msg}")
    if "data" not in data or not isinstance(data["data"], (dict, list)):
        raise ValidationError("Missing or malformed data field in response")
    return data