import logging

logger = logging.getLogger('crypto-tracker-45')

def validate_crypto_input(data: dict) -> bool:
    """Validate incoming crypto ticker data structure and values."""
    required_fields = ['symbol', 'price', 'volume']
    
    # Ensure all required keys are present
    if not all(field in data for field in required_fields):
        logger.warning("Missing required fields in input data: %s", data)
        return False
        
    symbol = data.get('symbol')
    price = data.get('price')
    volume = data.get('volume')
    
    # Validate symbol format
    if not isinstance(symbol, str) or not symbol.isalnum():
        logger.error("Invalid symbol format: %s", symbol)
        return False
        
    # Validate numeric ranges
    try:
        if float(price) <= 0 or float(volume) < 0:
            logger.error("Price and volume must be non-negative numbers: price=%s, volume=%s", price, volume)
            return False
    except (ValueError, TypeError):
        logger.error("Non-numeric values detected for price or volume")
        return False
        
    return True

def process_crypto_stream(stream_data: list):
    """Main processing loop with integrated input validation."""
    logger.info("Starting crypto stream processing loop")
    
    for entry in stream_data:
        if not validate_crypto_input(entry):
            logger.debug("Skipping invalid entry in stream")
            continue
            
        # Process valid cryptocurrency data
        clean_symbol = entry['symbol'].upper()
        clean_price = float(entry['price'])
        
        logger.info("Successfully processed %s at price %s", clean_symbol, clean_price)