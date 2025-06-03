import logging
import os


# The path for the logger file:
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "autoflex.log")

# Create a logger from logging:
logger = logging.getLogger("AutoFlexLogger")
logger.setLevel(logging.DEBUG)  # All levels (DEBUG -> INFO -> WARNING -> ERROR -> CRITICAL)

# Log format:
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)d - %(message)s"
)

# File logger handler:
file_handler = logging.FileHandler(log_file, encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Console logger handler:
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# Add both handlers to the logger instance:
logger.addHandler(file_handler)
logger.addHandler(console_handler)
