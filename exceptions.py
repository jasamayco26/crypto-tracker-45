class CryptoTrackerError(Exception):
    """Base exception for the crypto-tracker-45 application."""
    pass

class APIConnectionError(CryptoTrackerError):
    """Raised when the external crypto exchange API is unreachable."""
    pass

class RateLimitExceeded(CryptoTrackerError):
    """Raised when API requests exceed defined quota."""
    pass

class DataValidationError(CryptoTrackerError):
    """Raised when incoming market data fails structure checks."""
    pass

def handle_crypto_exception(e: Exception):
    """Logs and categorizes application-specific exceptions."""
    if isinstance(e, RateLimitExceeded):
        print(f"Warning: Rate limit reached. Backing off... {e}")
    elif isinstance(e, APIConnectionError):
        print(f"Critical: Network failure during fetch: {e}")
    elif isinstance(e, DataValidationError):
        print(f"Error: Invalid data schema received: {e}")
    else:
        print(f"Unexpected system failure: {str(e)}")
    return False