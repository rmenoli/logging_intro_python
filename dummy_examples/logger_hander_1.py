import logging

file_handler = logging.FileHandler("logfile.log")
file_handler.setLevel(logging.DEBUG)

logger = logging.getLogger()
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

logger.critical("Something critical")
logger.error("An error")
logger.warning("A warning")
logger.info("My info is that you are here")
logger.debug("I'm debugging")