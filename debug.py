from logging import getLogger, StreamHandler, INFO, DEBUG


def set_logger():
    logger = getLogger(__name__)
    logger.setLevel(DEBUG)
    logger.info('start logging debug')
    return logger


logger = set_logger()
