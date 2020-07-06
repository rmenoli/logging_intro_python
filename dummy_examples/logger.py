import logging

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

logger.critical("Something critical")
logger.error("An error")
logger.warning("A warning")
logger.info("My info is that you are here")
logger.debug("I'm debugging")