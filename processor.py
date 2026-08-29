from typing import Dict, Any, List

# Supported cryptocurrencies for the tracker
VALID_CRYPTOS = {'BTC', 'ETH', 'LTC', 'XRP', 'ADA'}

def validate_crypto_input(data: Dict[str, Any]) -> bool:
    if not isinstance(data, dict):
        return False
    if 'symbol' not in data or 'amount' not in data:
        return False
    symbol = data['symbol']
    amount = data['amount']
    if not isinstance(symbol, str) or symbol.upper() not in VALID_CRYPTOS:
        return False
    try:
        amount_float = float(amount)
        if amount_float <= 0:
            return False
    except (ValueError, TypeError):
        return False
    return True

def process_crypto_data(data: Dict[str, Any]) -> Dict[str, Any]:
    # Mock price data for simulation
    prices = {'BTC': 65000.0, 'ETH': 2600.0, 'LTC': 75.0, 'XRP': 0.55, 'ADA': 0.35}
    symbol = data['symbol'].upper()
    amount = float(data['amount'])
    price = prices.get(symbol, 0.0)
    total_value = amount * price
    return {'symbol': symbol, 'amount': amount, 'current_price': price, 'total_value_usd': total_value}

def main_processing_loop(input_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    # Main processing loop with input validation
    processed_results = []
    for idx, input_data in enumerate(input_list):
        # Validate input before any processing
        if not validate_crypto_input(input_data):
            print(f"Invalid input skipped at {idx}: {input_data}")
            continue
        try:
            result = process_crypto_data(input_data)
            processed_results.append(result)
            print(f"Processed {result['symbol']}: value {result['total_value_usd']}")
        except Exception as e:
            print(f"Error: {e}")
    return processed_results

if __name__ == "__main__":
    sample_data = [
        {'symbol': 'BTC', 'amount': 0.5},
        {'symbol': 'eth', 'amount': '1.2'},
        {'symbol': 'DOGE', 'amount': 100},
        {'symbol': 'LTC', 'amount': '0'},
        {'symbol': 'XRP', 'amount': 200},
    ]
    results = main_processing_loop(sample_data)
    print("Results:", results)