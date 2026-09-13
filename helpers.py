import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "api_base_url": "https://api.coingecko.com/api/v3",
    "request_timeout": 30,
    "currency": "usd",
    "update_interval": 60
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from disk with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load config file: {e}. Using defaults.")
    
    return config

def validate_config(config: Dict[str, Any]) -> bool:
    """Ensures required configuration keys are present and valid."""
    required_keys = ["api_base_url", "currency"]
    return all(key in config for key in required_keys)