import pandas as pd
from datetime import datetime


IN_FOLDER = 'output'
IN_FILE = 'flight_route_locations'

OUT_FOLDER = 'db/data'
OUT_FILE = 'flight_data'

TABLE = 'Flight'
KEYS = ['tail_no', 'flight_timestamp']

FILE_LINES_MAX = 500000


flight_df = pd.read_csv(f'{IN_FOLDER}/{IN_FILE}.csv')
flight_df.drop_duplicates(subset=KEYS, keep='first', inplace=True)

num = 1
i = 0

while i < len(flight_df):
    count = 0

    with open(f'{OUT_FOLDER}/{OUT_FILE}{num}.sql', 'w') as f:
        f.write(f'INSERT INTO {TABLE} VALUES\n')

        while count < FILE_LINES_MAX and i < len(flight_df):
            row = flight_df.iloc[i]
            date = str(datetime.fromisoformat(row["flight_timestamp"]))[:-6]
            
            s = f'  (\'{row["tail_no"]}\', \'{row["flight_id"]}\', \'{date}\','
            s += f' {row["latitude"]}, {row["longitude"]}, {row["altitude"]},'
            s += f' \'{row["altitude_change"]}\', {row["ground_speed"]}, {row["heading"]})'
            s += (',' if (count < FILE_LINES_MAX - 1) and (i < len(flight_df) - 1) else ';') + '\n'
            
            f.write(s)
            
            count += 1
            i += 1
    
    num += 1
