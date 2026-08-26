import logging
import os
from datetime import datetime
from typing import Optional


def get_logger(name: str = "crypto_tracker") -> logging.Logger:
    """Get or create a logger for the crypto tracker."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        # Console handler for real-time output
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_format = logging.Formatter(
            '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        console_handler.setFormatter(console_format)
        logger.addHandler(console_handler)

        # File handler for persistent logs
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        file_handler = logging.FileHandler(
            os.path.join(log_dir, f"{name}.log")
        )
        file_handler.setLevel(logging.DEBUG)
        file_format = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(file_format)
        logger.addHandler(file_handler)
    return logger


def log_price_update(logger: logging.Logger, symbol: str, price: float, timestamp: Optional[datetime] = None) -> None:
    """Log a price update for a crypto symbol."""
    if timestamp is None:
        timestamp = datetime.now()
    message = f"Price update: {symbol} = ${price:.2f} at {timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
    logger.info(message)


def log_trade_execution(logger: logging.Logger, symbol: str, action: str, amount: float, price: float) -> None:
    """Log a trade execution."""
    message = f"Trade executed: {action} {amount} {symbol} at ${price:.2f}"
    logger.info(message)


def log_error(logger: logging.Logger, error: Exception, context: str = "") -> None:
    """Log an error with optional context."""
    message = f"Error in {context}: {str(error)}" if context else f"Error: {str(error)}"
    logger.error(message)


def log_warning(logger: logging.Logger, message: str) -> None:
    """Log a warning message."""
    logger.warning(message)


def log_debug(logger: logging.Logger, message: str) -> None:
    """Log a debug message."""
    logger.debug(message)