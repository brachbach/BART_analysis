import pandas as pd

df = pd.read_csv('raw_data/date-hour-soo-dest-2019.csv', names=["Day", "Hour", "Origin Station", "Destination Station", "Trip Count"])

# Saturday, Sunday, Monday, Tuesday, Wednesday from two recent weeks
five_days = df.loc[df['Day'].isin(["2019-08-17", "2019-08-11", "2019-08-19", "2019-08-13", "2019-08-21"])]
five_days.to_csv(path_or_buf="processed_data/five_days.csv")