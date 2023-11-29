# This script will read in the cleaned fire data and 
# output a MySQL script to insert rows into the FirePoint table
import pandas as pd


IN_FOLDER = 'output'
IN_FILE = 'frontend_fire_data_no_nan'

OUT_FOLDER = 'db'
OUT_FILE = 'fire_data'

TABLE = 'FirePoint'


fire_df = pd.read_csv(f'{IN_FOLDER}/{IN_FILE}.csv')


with open(f'{OUT_FOLDER}/{OUT_FILE}.sql', 'w') as f:
    f.write(f'INSERT INTO {TABLE} VALUES\n')

    for i in range(len(fire_df)):
        row = fire_df.iloc[i]

        s = f'  (\'{row["CreatedOnDateTime_dt"][:-6]}\', {row["Latitude"]}, {row["Longitude"]})'
        s += (',' if i < (len(fire_df) - 1) else ';') + '\n'
        
        f.write(s)
