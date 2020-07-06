import pandas as pd
import utils
import os
p = os.path.dirname(os.path.realpath(__file__))

def main():
    try:
        model = utils.read_model()
        data = pd.read_csv(p +"/data/weather_data.csv")
    except:
        print("Problem in loading")
        return -1
    
    last_row = data[-1:]
    
    if not utils.is_last_data_is_new(last_row):
        print("last data not new")
        return -1
    
    prevision = model.make_prevision(last_row)
    prevision.display()
    
    print("done!")
    return 0
 
if __name__ == "__main__":
    main()