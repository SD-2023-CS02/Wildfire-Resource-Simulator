import pandas as pd
from datetime import datetime


IN_FOLDER = '.'
IN_FILE = 'flight_results'

OUT_FOLDER = 'db/data'
OUT_FILE = 'flightinfo_data'

TABLE = 'FlightInfo'

NULL = 'NULL'
NAN = 'nan'


flight_info_df = pd.read_csv(f'{IN_FOLDER}/{IN_FILE}.csv')
flight_info_df.dropna(subset=['takeoff', 'landing'], inplace=True)
missing_rows_df = pd.read_csv('missing_rows.csv')
missing_rows_df.dropna(subset=['takeoff', 'landing'], inplace=True)


with open(f'{OUT_FOLDER}/{OUT_FILE}.sql', 'w') as f:
    f.write(f'INSERT INTO {TABLE} VALUES\n')

    for i in range(len(flight_info_df)):
        row = flight_info_df.iloc[i]
        
        source = f'\'{row["source"]}\'' if str(row["source"]) != NAN else NULL
        destination = f'\'{row["destination"]}\'' if str(row["destination"]) != NAN else NULL
        takeoff = str(datetime.fromisoformat(row["takeoff"]))
        landing = str(datetime.fromisoformat(row["landing"]))
        
        s = f'  (\'{row["flight_id"]}\', {source}, {destination}, \'{takeoff}\', \'{landing}\'),\n'
        
        f.write(s)
    '''
    for i in range(len(missing_rows_df)):
        row = missing_rows_df.iloc[i]

        source = f'\'{row["source"]}\'' if str(row["source"]) != NAN else NULL
        destination = f'\'{row["destination"]}\'' if str(row["destination"]) != NAN else NULL
        
        s = f'  (\'{row["flight_id"]}\', {source}, {destination}, \'{row["takeoff"]}\', \'{row["landing"]}\')'
        s += (',' if i < (len(missing_rows_df) - 1) else ';') + '\n'

        f.write(s)
    '''
