import re

class InputValidator:
    """Validator for cryptocurrency processing inputs."""

    SYMBOL_PATTERN = re.compile(r'^[A-Z0-9]{2,10}$')

    @staticmethod
    def validate_ticker(ticker: str) -> bool:
        """Checks if the ticker format is compliant."""
        if not isinstance(ticker, str):
            return False
        return bool(InputValidator.SYMBOL_PATTERN.match(ticker.upper()))

    @staticmethod
    def validate_amount(amount: float) -> bool:
        """Ensures the trade amount is positive."""
        return isinstance(amount, (int, float)) and amount > 0

    @staticmethod
    def validate_payload(data: dict) -> bool:
        """
        Validates incoming processing request data.
        Expected keys: 'ticker', 'amount'
        """
        required_keys = {'ticker', 'amount'}
        if not all(key in data for key in required_keys):
            return False

        return (
            InputValidator.validate_ticker(data['ticker']) and
            InputValidator.validate_amount(data['amount'])
        )

    @staticmethod
    def sanitize_input(data: dict) -> dict:
        """Normalizes data fields for processing."""
        return {
            'ticker': str(data['ticker']).strip().upper(),
            'amount': float(data['amount'])
        }