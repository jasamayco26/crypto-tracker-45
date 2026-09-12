import logging
from typing import Dict, Any, Optional

# Configure logging for crypto-tracker-45
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def format_crypto_data(data: Dict[str, Any]) -> Optional[Dict[str, float]]:
    """
    Sanitizes and normalizes crypto price data from external APIs.
    Expects dict containing 'symbol' and 'price_usd'.
    """
    try:
        symbol = data.get('symbol', 'UNKNOWN').upper()
        price = float(data.get('price_usd', 0.0))
        
        if price < 0:
            logger.warning(f"Negative price detected for {symbol}: {price}")
            return None
            
        return {
            "symbol": symbol,
            "price": round(price, 8),
            "source": "api-v1"
        }
    except (ValueError, TypeError) as e:
        logger.error(f"Data normalization failure: {e}")
        return None

def calculate_percentage_change(current: float, previous: float) -> float:
    """
    Computes simple percentage change between two price points.
    """
    if previous == 0:
        return 0.0
    return ((current - previous) / previous) * 100