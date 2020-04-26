from logging import getLogger, StreamHandler, INFO, DEBUG


def set_logger():
    logger = getLogger(__name__)
    handler = StreamHandler()
    handler.setLevel(DEBUG)
    logger.setLevel(DEBUG)
    logger.addHandler(handler)
    logger.info('start logging debug')
    return logger


logger = set_logger()
