import random
import pandas as pd

COL = ["HUMIDITY", "AIR_PRESSURE", "WIND_SPEED", "CLOUD_PRESENCE"]

class weather_api():
    @staticmethod
    def get_value():
        working_trigger = random.random()
        if working_trigger > 0.9:
            raise Exception(f"something wrong")
        return random.random()

class HumidityApi(weather_api):
    pass

class AirPressureApi(weather_api):
    pass

class WindSpeedApi(weather_api):
    pass

class CloudsNearbyApi(weather_api):
    pass

class Prevision():
    def __init__(self, time, forecast):
        self.time = time
        self.forecast = forecast
        
    def display(self):
        print(f"weather forecast for {self.time} is {self.forecast}")
        
        
class WeatherModel():
    def make_prevision(self,row):
        if row.sum(axis=1).values[0]<1:
            return Prevision(pd.Timestamp.now(), "RAINING :(")
        else:
            return Prevision(pd.Timestamp.now(),"SUNNY :)")

def append_new_row(df, values):
    df_new = pd.DataFrame([values], columns= COL)
    df_out = pd.concat([df, df_new], sort=False, ignore_index=True)
    return df_out

def read_model():
    working_trigger = random.random()
    if working_trigger > 0.7:
        raise Exception("Model not loaded")
    model = WeatherModel()
    return model

def is_last_data_is_new(row):
    return True