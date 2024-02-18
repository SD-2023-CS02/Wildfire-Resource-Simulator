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
NAN = 'nan'
#KEYS = ['CreatedOnDateTime_dt', 'Latitude', 'Longitude']


fire_df = pd.read_csv(f'{IN_FOLDER}/{IN_FILE}.csv')
#fire_df.drop_duplicates(subset=KEYS, keep='first', inplace=True) # temporary solution for dropping duplicate incident locations+dates


with open(f'{OUT_FOLDER}/{OUT_FILE}.sql', 'w', errors='ignore') as f:
    f.write(f'INSERT INTO {TABLE} VALUES\n')
    
    for i in range(len(fire_df)):
        row = fire_df.iloc[i]
        
        fire_id = str(row['UniqueFireIdentifier']).replace('\'', '\\\'').replace('"', '\\"')
        incident_name = str(row['IncidentName']).replace('\'', '\\\'').replace('"', '\\"')

        initial_lat = f'\'{row["InitialLatitude"]}\'' if str(row['InitialLatitude']) != NAN else NULL
        initial_long = f'\'{row["InitialLongitude"]}\'' if str(row['InitialLongitude']) != NAN else NULL
        gacc = f'\'{row["GACC"]}\'' if str(row['GACC']) != NAN else NULL

        containment_date = f'\'{row["ContainmentDateTime"][:-6]}\'' if row['ContainmentDateTime'] is not np.nan else NULL
        fireout_date = f'\'{row["FireOutDateTime"][:-6]}\'' if row["FireOutDateTime"] is not np.nan else NULL
        control_date = f'\'{row["ControlDateTime"][:-6]}\'' if row["ControlDateTime"] is not np.nan else NULL

        discovery_acres = row['DiscoveryAcres'] if str(row['DiscoveryAcres']) != NAN else NULL
        incident_size = row['IncidentSize'] if str(row['IncidentSize']) != NAN else NULL
        final_acres = row['FinalAcres'] if str(row['FinalAcres']) != NAN else NULL
        initial_acres = row['InitialResponseAcres'] if str(row['InitialResponseAcres']) != NAN else NULL

        s = f'  (\'{fire_id}\', \'{incident_name}\','
        s += f' \'{row["CreatedOnDateTime_dt"][:-6]}\', \'{row["FireDiscoveryDateTime"][:-6]}\','
        s += f' {row["Latitude"]}, {row["Longitude"]}, {initial_lat}, {initial_long}, {gacc},'
        s += f' {containment_date}, {fireout_date}, {control_date},'
        s += f' {discovery_acres}, {incident_size}, {final_acres}, {initial_acres})'
        s += (',' if i < (len(fire_df) - 1) else ';') + '\n'
        
        f.write(s)
