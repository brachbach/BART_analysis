import os, json
import pandas as pd

dir_path = 'raw_data/real_time_departures'

filenames = os.listdir(dir_path)

filepaths = [f"{dir_path}/{filename}" for filename in filenames]

parsed_jsons = [json.load(open(filepath)) for filepath in filepaths]


def get_new_date_time(orig_date, orig_time, additional_min_str):
    addtl_min = 0
    try:
        addtl_min = int(additional_min_str)
    except:
        print(additional_min_str)
    return pd.to_datetime(f"{orig_date} {orig_time}") + pd.Timedelta(addtl_min, unit="m")

formatted_jsons = [
    [   
        [
            {
                'time': get_new_date_time(parsed_json['root']['date'], parsed_json['root']['time'], estimate['minutes']),
                'length': estimate['length']
            }
            for estimate in etd['estimate']
        ]
        for etd in parsed_json['root']['station'][0]['etd']
    ] for parsed_json in parsed_jsons
]

times_and_lengths = [time_and_length for formatted_json in formatted_jsons for etd in formatted_json for time_and_length in etd]

times_and_lengths_df = pd.DataFrame(times_and_lengths)

times_and_lengths_df.to_csv(path_or_buf="processed_data/rtds.csv")
