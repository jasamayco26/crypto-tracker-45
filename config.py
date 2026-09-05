import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "COINGECKO_API_KEY": "",
    "UPDATE_INTERVAL_SECONDS": 60,
    "DEFAULT_FIAT_CURRENCY": "usd",
    "TRACKED_CRYPTOS": ["bitcoin", "ethereum", "solana"],
    "LOG_LEVEL": "INFO",
    "ALERT_THRESHOLD_PERCENT": 5.0
}

class ConfigLoader:
    """Loads and parses tracker configuration from file and environment variables."""

    def __init__(self, config_path: str = None) -> None:
        self.config_path = config_path
        self._config: Dict[str, Any] = DEFAULT_CONFIG.copy()
        self._load()

    def _load(self) -> None:
        # Load from optional JSON file
        if self.config_path and os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_data = json.load(f)
                    if isinstance(file_data, dict):
                        self._config.update(file_data)
            except (json.JSONDecodeError, OSError):
                pass  # Fall back to defaults on parsing errors

        # Override with environment variables
        for key, default_val in DEFAULT_CONFIG.items():
            env_val = os.getenv(key)
            if env_val is not None:
                if isinstance(default_val, list):
                    self._config[key] = [item.strip() for item in env_val.split(",") if item.strip()]
                elif isinstance(default_val, int):
                    self._config[key] = int(env_val)
                elif isinstance(default_val, float):
                    self._config[key] = float(env_val)
                else:
                    self._config[key] = env_val

    def get(self, key: str) -> Any:
        """Retrieve a configured value by its key."""
        return self._config.get(key)