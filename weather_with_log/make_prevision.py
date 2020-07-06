import pandas as pd
import utils
import os
from mylogger import getmylogger
p = os.path.dirname(os.path.realpath(__file__))


logger = getmylogger(__name__)

def main():
    logger.info("Make prevision started")
    try:
        model = utils.read_model()
        data = utils.read_data()
    except:
        logger.critical("Problem in loading data")
        return -1
    
    last_row = data[-1:]
    
    if not utils.is_last_data_is_new(last_row):
        logger.warning("last data not new")
        return -1
    
    prevision = model.make_prevision(last_row)
    prevision.display()
    
    logger.info("Make prevision ended withou errors")
    return 0
 
if __name__ == "__main__":
    main()