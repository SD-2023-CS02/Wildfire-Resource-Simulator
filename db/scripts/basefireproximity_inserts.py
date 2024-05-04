import pandas as pd


IN_FOLDER = 'output'
IN_FILE = 'base_fire_proximity'

OUT_FOLDER = 'db/data'
OUT_FILE = 'basefireproximity_data'

TABLE = 'BaseFireProximity'


prox_df = pd.read_csv(f'{IN_FOLDER}/{IN_FILE}.csv')


with open(f'{OUT_FOLDER}/{OUT_FILE}.sql', 'w') as f:
    f.write(f'INSERT INTO {TABLE} VALUES\n')

    for i in range(len(prox_df)): 
        row = prox_df.iloc[i]

        s = f'  (\'{row["base_code"]}\', {row["proximity"]})'
        s += (',' if i < (len(prox_df) - 1) else ';') + '\n'

        f.write(s)
