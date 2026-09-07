import logging
from typing import Any, Dict

def validate_ticker_data(data: Dict[str, Any]) -> bool:
    """Validates incoming crypto ticker payload structure."""
    required_fields = ['symbol', 'price', 'timestamp']
    
    try:
        if not isinstance(data, dict):
            return False
        
        if not all(field in data for field in required_fields):
            logging.warning(f"Missing fields in data: {data}")
            return False
            
        if not isinstance(data['price'], (int, float)) or data['price'] < 0:
            logging.warning(f"Invalid price value: {data.get('price')}")
            return False
            
        return True
    except Exception as e:
        logging.error(f"Validation runtime error: {e}")
        return False

def sanitize_input(symbol: str) -> str:
    """Cleans user input to prevent injection."""
    return ''.join(char for char in symbol if char.isalnum()).upper()