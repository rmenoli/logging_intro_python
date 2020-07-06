import logging
import os
p = os.path.dirname(os.path.realpath(__file__))

def getmylogger(name):
    file_formatter = logging.Formatter('%(asctime)s~%(levelname)s~%(message)s~module:%(module)s')
    console_formatter = logging.Formatter('%(levelname)s -- %(message)s')
    
    file_handler = logging.FileHandler(p+"/logfile.log")
    file_handler.setLevel(logging.WARN)
    file_handler.setFormatter(file_formatter)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(console_formatter)

    logger = logging.getLogger()
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.setLevel(logging.DEBUG)
    
    return logger