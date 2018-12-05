import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def info(msg):
    logger.info(msg)


def error(msg):
    logger.error(msg)


def debug(msg):
    logger.debug(msg)
