import pandas as pd


IN_FOLDER = 'output'
IN_FILE = 'plane_drops_results_full'

OUT_FOLDER = 'db/data'
OUT_FILE = 'planedrops_data'

TABLE = 'PlaneDrops'


drops_df = pd.read_csv(f'{IN_FOLDER}/{IN_FILE}.csv')


with open(f'{OUT_FOLDER}/{OUT_FILE}.sql', 'w') as f:
    f.write(f'INSERT INTO {TABLE} VALUES\n')

    for i in range(len(drops_df)):
        row = drops_df.iloc[i]

        s = f'  (\'{row["fire_id"]}\', \'{row["tail_no"]}\','
        s += f' \'{row["flight_id"]}\', \'{row["flight_timestamp"]}\')'
        s += (',' if i < (len(drops_df) - 1) else ';') + '\n'

        f.write(s)
