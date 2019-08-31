import requests
import pandas as pd
import json
from datetime import datetime
from threading import Timer

route = "etd.aspx"

params = {
    "cmd": "etd",
    "orig": "embr",
    "key": "MW9S-E7SL-26DU-VV8V",
    "json": "y"
}

def get_current_data():
    schedule = requests.get(f"https://api.bart.gov/api/{route}", params=params)

    with open(f"raw_data/real_time_departures/{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}.json", 'w') as outfile:
        json.dump(schedule.json(), outfile)

    t = Timer(60.0 * 10, get_current_data)
    t.start()

get_current_data()
# schedule_df = pd.DataFrame(schedule.json()['root']['station']['etd'])