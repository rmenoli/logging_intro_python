import pandas as pd
import utils
import os
from mylogger import getmylogger
p = os.path.dirname(os.path.realpath(__file__))

logger = getmylogger(__name__)

def main():
    logger.info("Ingestion stared")
    features_apis = [utils.HumidityApi, utils.AirPressureApi, 
                    utils.WindSpeedApi, utils.CloudsNearbyApi]
    fetures_values = []
    for feature_api in features_apis:
        try:
            f_value = feature_api.get_value()
        except:
            logger.critical(f"API {feature_api} is not working")
            return -1
        
        fetures_values.append(f_value)
        
    df_weather = pd.read_csv(p +"/data/weather_data.csv")
    df_weather = utils.append_new_row(df_weather, fetures_values)
    df_weather.to_csv(p +"/data/weather_data.csv", index=False)
    
    logger.info("Ingestion ended without errors")
    
    return 0
 
if __name__ == "__main__":
    main()