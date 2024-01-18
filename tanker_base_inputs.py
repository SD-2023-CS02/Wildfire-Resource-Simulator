# This script will read in the parsed tanker base data from the pdf and
# output a MySQL script to insert rows into the TankerBase table
import pandas as pd
import numpy as np


IN_FOLDER = 'output'
IN_FILE = 'tanker_bases'

OUT_FILE = 'base_data'

TABLE = 'TankerBase'

NULL = 'NULL'
KEYS = ["Base Name", "Airport", "Latitude, Longitude", "Geographic Area", "Runway Weight Limits", 
        "VLATs", "LATs", "MAFFS"]  


base_df = pd.read_csv(f'{IN_FOLDER}/{IN_FILE}.csv')

with open(f'{OUT_FILE}.sql', 'w') as f:
    f.write(f'INSERT INTO {TABLE} VALUES\n')

# EDIT BELOW THIS POINT
    for i in range(len(base_df)): 
        row = base_df.iloc[i]

        base_name = row["Base Name"]
        airport = row["Airport"]
        lat_long = row['Latitude, Longitude']
        geo_area = row["Geographic Area"]
        runway_wt_lim = row["Runway Weight Limits"]
        vlat_values = row["VLATs"]
        lat_values = row["LATs"]
        maffs_values = row["MAFFS"]

        s = (f' ({base_name}, {airport}, {lat_long}, {geo_area}, {runway_wt_lim}, ' + 
             f'{vlat_values}, {lat_values}, {maffs_values})')
        s += (',' if i < (len(base_df) - 1) else ';') + '\n'

        f.write(s)