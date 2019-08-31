import os, json
import pandas as pd

parsed_jsons = []
for json_file in os.listdir('raw_data/real_time_departures'):
    with open(f"raw_data/real_time_departures/{json_file}") as json_file:
        data = json.load(json_file)
        parsed_jsons.append(data)

print(parsed_jsons[0])
