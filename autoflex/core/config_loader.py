import yaml
import os
from .logger import logger
from .exceptions import ConfigLoadError



def load_config(config_path=None):
    """
    Load YAML configurations, return a dict
    """
    default_path = os.path.join(os.path.dirname(__file__), "../config/config.yaml")
    final_path = config_path if config_path else default_path
    try:
        # Check if the path exists:
        if not os.path.exists(final_path):
            raise FileNotFoundError(f"No Configuration File Found: {final_path}")

        # Open and analyze YAML file:
        with open(final_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)

        logger.info(f"Successfully Loaded The Configuration File: {final_path}")
        return config

    except Exception as e:
        logger.error(f"Failed To Load The Configuration File: {str(e)}")
        raise ConfigLoadError("Failed To Load Configuration File.", e)
