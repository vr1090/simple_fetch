import logging
import sys

def get_logger():
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler(sys.stdout)

    if not logger.hasHandlers() :
        logger.addHandler(handler)
    
    logger.setLevel(logging.DEBUG)
    return logger
