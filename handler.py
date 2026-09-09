from typing import List, Dict, Optional
import decimal

def format_crypto_data(raw_data: List[Dict]) -> List[Dict]:
    """Cleans and standardizes crypto market data from API responses."""
    processed = []
    
    for item in raw_data:
        try:
            # Standardize numeric values as Decimals for precision
            price = decimal.Decimal(str(item.get('price', 0)))
            volume = decimal.Decimal(str(item.get('volume_24h', 0)))
            
            processed.append({
                'symbol': str(item.get('symbol', 'UNKNOWN')).upper(),
                'price': price,
                'volume': volume,
                'is_active': item.get('status') == 'active'
            })
        except (decimal.InvalidOperation, ValueError, TypeError):
            continue
            
    return processed

def filter_by_volume(data: List[Dict], min_volume: decimal.Decimal) -> List[Dict]:
    """Filters crypto list based on 24h trading volume."""
    return [d for d in data if d['volume'] >= min_volume]

def calculate_market_cap(price: decimal.Decimal, supply: decimal.Decimal) -> decimal.Decimal:
    """Computes estimated market capitalization."""
    return (price * supply).quantize(decimal.Decimal('0.01'))