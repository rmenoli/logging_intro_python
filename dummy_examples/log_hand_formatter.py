import logging

formatter = logging.Formatter('%(asctime)s~%(levelname)s~%(message)s~module:%(module)s')

file_handler = logging.FileHandler("logfile.log")
file_handler.setLevel(logging.WARN)
file_handler.setFormatter(formatter)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)

logger.critical("Something critical")
logger.error("An error")
logger.warning("A warning")
logger.info("My info is that you are here")
logger.debug("I'm debugging")