import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "api_url": "https://api.crypto-tracker.io/v1",
    "refresh_interval": 60,
    "log_level": "INFO",
    "max_retries": 3
}

def load_config(path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from file with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load {path}: {e}. Using defaults.")
            
    return config

def get_config_value(key: str, path: str = "config.json") -> Any:
    """Retrieves a single configuration key value."""
    cfg = load_config(path)
    return cfg.get(key, DEFAULT_CONFIG.get(key))