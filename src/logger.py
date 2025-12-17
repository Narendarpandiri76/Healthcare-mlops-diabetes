import logging
import os
from datetime import datetime


LOG_DIR = "logs"
LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
LOG_PATH = os.path.join(LOG_DIR, LOG_FILE)

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH,
    format="[ %(asctime)s ] %(levelname)s %(name)s : %(message)s",
    level=logging.INFO,
)

def get_logger(name: str):
    """
    Returns a configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger
