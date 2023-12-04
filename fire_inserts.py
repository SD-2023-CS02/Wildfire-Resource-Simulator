# This script will read in the cleaned fire data and 
# output a MySQL script to insert rows into the FirePoint table
import pandas as pd
import numpy as np


IN_FOLDER = 'output'
IN_FILE = 'frontend_fire_data'

OUT_FOLDER = 'db'
OUT_FILE = 'fire_data'

TABLE = 'FirePoint'

NULL = 'NULL'
KEYS = ['CreatedOnDateTime_dt', 'Latitude', 'Longitude']


fire_df = pd.read_csv(f'{IN_FOLDER}/{IN_FILE}.csv')
fire_df.drop_duplicates(subset=KEYS, keep='first', inplace=True) # temporary solution for dropping duplicate incident locations+dates


with open(f'{OUT_FOLDER}/{OUT_FILE}.sql', 'w') as f:
    f.write(f'INSERT INTO {TABLE} VALUES\n')

    for i in range(len(fire_df)):
        row = fire_df.iloc[i]
        
        containment_time = f'\'{row["ContainmentDateTime"][:-6]}\'' if row['ContainmentDateTime'] is not np.nan else NULL
        fire_out_time = f'\'{row["FireOutDateTime"][:-6]}\'' if row["FireOutDateTime"] is not np.nan else NULL
        discovery_acres = row['DiscoveryAcres'] if str(row['DiscoveryAcres']) != 'nan' else NULL
        incident_size = row['IncidentSize'] if str(row['IncidentSize']) != 'nan' else NULL

        s = (f'  (\'{row["CreatedOnDateTime_dt"][:-6]}\', {row["Latitude"]}, {row["Longitude"]}, ' +
             f'{containment_time}, {fire_out_time}, {discovery_acres}, {incident_size})')
        s += (',' if i < (len(fire_df) - 1) else ';') + '\n'
        
        f.write(s)
