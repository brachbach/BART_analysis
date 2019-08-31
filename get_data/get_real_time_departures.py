import requests
import pandas as pd
import json
from datetime import datetime

route = "etd.aspx"

params = {
    "cmd": "etd",
    "orig": "embr",
    "key": "MW9S-E7SL-26DU-VV8V",
    "json": "y"
}

schedule = requests.get(f"https://api.bart.gov/api/{route}", params=params)

with open(f"raw_data/real_time_departures/{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}", 'w') as outfile:
    json.dump(schedule.json(), outfile)

# schedule_df = pd.DataFrame(schedule.json()['root']['station']['etd'])