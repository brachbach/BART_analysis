import requests
import pandas as pd

public_api_key = 'MW9S-E7SL-26DU-VV8V'

schedule = requests.get('https://api.bart.gov/api/sched.aspx?cmd=stnsched&orig=embr&key=MW9S-E7SL-26DU-VV8V&date=08/13/2019&json=y')

schedule_df = pd.DataFrame(schedule.json()['root']['station']['item'])

schedule_df.to_csv(path_or_buf="processed_data/08-13-2019-embr-sched.csv")