import requests
from typing import Dict, List, Optional

def fetch_current_price(crypto_id: str, vs_currency: str = "usd") -> Optional[float]:
    """Fetch the current price of a cryptocurrency."""
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {"ids": crypto_id, "vs_currencies": vs_currency}
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get(crypto_id, {}).get(vs_currency)
    except Exception:
        return None

def calculate_percentage_change(previous_price: float, current_price: float) -> float:
    """Calculate the percentage change in price."""
    if previous_price == 0:
        return 0.0
    change = ((current_price - previous_price) / previous_price) * 100
    return round(change, 2)

def format_price(price: float, currency: str = "USD") -> str:
    """Format a price value for display."""
    return f"{price:,.2f} {currency.upper()}"

def calculate_portfolio_value(holdings: Dict[str, float], prices: Dict[str, float]) -> float:
    """Calculate total value of crypto portfolio."""
    total = 0.0
    for crypto, amount in holdings.items():
        if crypto in prices:
            total += amount * prices[crypto]
    return round(total, 2)

def get_trend_direction(prices: List[float]) -> str:
    """Determine price trend direction from list of prices."""
    if len(prices) < 2:
        return "unknown"
    change = calculate_percentage_change(prices[0], prices[-1])
    if change > 1:
        return "up"
    elif change < -1:
        return "down"
    return "stable"