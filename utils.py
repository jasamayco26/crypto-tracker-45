from typing import Dict, List, Optional, Union
from decimal import Decimal

def format_currency(amount: Union[float, Decimal], symbol: str = "USD") -> str:
    """Formats a numeric amount into a localized currency string."""
    return f"{symbol} {amount:,.2f}"

def calculate_percentage_change(current: float, previous: float) -> float:
    """Calculates the percentage difference between two crypto prices."""
    if previous == 0:
        return 0.0
    return ((current - previous) / previous) * 100

def filter_assets_by_volume(data: List[Dict[str, Union[str, float]]], min_volume: float) -> List[Dict[str, Union[str, float]]]:
    """Returns assets exceeding a specific trading volume threshold."""
    return [asset for asset in data if asset.get("volume", 0) >= min_volume]

def parse_api_response(response: Optional[Dict]) -> Dict:
    """Extracts price data from standard exchange API responses."""
    if not response or "data" not in response:
        return {}
    return response["data"]