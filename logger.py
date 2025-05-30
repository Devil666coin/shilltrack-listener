import logging

def setup_logger(name: str, log_file: str, level=logging.INFO):
    handler = logging.FileHandler(log_file, mode='a')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    logger.propagate = False

    return logger

logger = setup_logger('mention_logger', 'mentions.log')