import pandas as pd


IN_FOLDER = 'data'
IN_FILE = 'airtankers'

OUT_FOLDER = 'db/data'
OUT_FILE = 'fireplane_data'

TABLE = 'FirePlane'


plane_df = pd.read_csv(f'{IN_FOLDER}/{IN_FILE}.csv')


with open(f'{OUT_FOLDER}/{OUT_FILE}.sql', 'w') as f:
    f.write(f'INSERT INTO {TABLE} VALUES\n')

    for i in range(len(plane_df)): 
        row = plane_df.iloc[i]

        s = f'  (\'{row["N #"]}\', \'{row["Tank Type"]}\', \'{row["Contractor"]}\')'
        s += (',' if i < (len(plane_df) - 1) else ';') + '\n'

        f.write(s)
