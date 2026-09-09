import math
from typing import Dict, Optional, Union

class CryptoHandler:
    """Helper class for handling cryptocurrency price calculations and formatting."""

    def __init__(self, default_fiat: str = "USD"):
        self.default_fiat = default_fiat.upper()

    def calculate_percentage_change(self, old_price: float, new_price: float) -> float:
        """Calculate the percentage change between two price points."""
        if old_price <= 0:
            raise ValueError("Initial price must be greater than zero.")
        change = ((new_price - old_price) / old_price) * 100
        return round(change, 2)

    def convert_fiat_to_crypto(self, fiat_amount: float, crypto_price: float) -> float:
        """Determine how much cryptocurrency can be purchased with a given fiat amount."""
        if crypto_price <= 0:
            raise ValueError("Cryptocurrency price must be greater than zero.")
        if fiat_amount < 0:
            raise ValueError("Fiat amount cannot be negative.")
        return round(fiat_amount / crypto_price, 8)

    def format_price(self, price: float, currency_symbol: str = "$") -> str:
        """Format a price value nicely, handling micro-cents for cheap assets."""
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        if price >= 1.0:
            return f"{currency_symbol}{price:,.2f}"
        elif price > 0:
            # For cheap assets, dynamically adjust decimal precision
            decimals = max(2, min(8, int(-math.log10(price)) + 2))
            return f"{currency_symbol}{price:,.{decimals}f}"
        return f"{currency_symbol}0.00"