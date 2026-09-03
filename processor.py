import logging
from typing import Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def validate_crypto_data(data: Dict[str, Any]) -> bool:
    """Validates the incoming crypto tracking payload."""
    if not isinstance(data, dict):
        return False
    
    required_fields = ["symbol", "price", "volume"]
    for field in required_fields:
        if field not in data:
            logging.warning(f"Validation failed: Missing field '{field}'")
            return False
            
    if not isinstance(data["symbol"], str) or not data["symbol"].isalpha():
        logging.warning("Validation failed: 'symbol' must be an alphabetic string")
        return False
        
    try:
        price = float(data["price"])
        volume = float(data["volume"])
        if price <= 0 or volume < 0:
            logging.warning("Validation failed: 'price' and 'volume' must be positive numbers")
            return False
    except (TypeError, ValueError):
        logging.warning("Validation failed: 'price' and 'volume' must be numeric values")
        return False
        
    return True

def process_stream(payloads: list) -> None:
    """Main processing loop with input validation for crypto tracker."""
    for index, payload in enumerate(payloads):
        logging.info(f"Processing payload index {index}")
        if not validate_crypto_data(payload):
            logging.error(f"Skipping invalid payload at index {index}")
            continue
            
        # Process validated payload
        symbol = payload["symbol"].upper()
        price = float(payload["price"])
        volume = float(payload["volume"])
        market_cap = price * volume
        
        logging.info(f"Successfully processed {symbol}: Price ${price:.2f}, Market Cap estimation: ${market_cap:.2f}")
